from faststream import FastStream
from faststream.kafka import KafkaBroker
import json
import importlib
import asyncio
from dotenv import load_dotenv
import os
import time
import logging
import boto3

# Load environment variables from .env file
load_dotenv(dotenv_path = '.env')

broker = KafkaBroker(os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"))
app = FastStream(broker)

validation_modules_cache = {}
domains_to_validate = [domain.strip() for domain in os.getenv("DOMAIN_TO_VALIDATE", "ONDC:RET10").split(",")]
validation_success_topic = os.getenv("KAFKA_VALIDATIONS_SUCCESS_TOPIC", "validations-done")
validation_missing_topic = os.getenv("KAFKA_VALIDATIONS_MISSING_TOPIC", "validations-missing")

cw_client = boto3.client('cloudwatch', region_name=os.getenv("AWS_REGION", "ap-south-1"))

def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s] %(filename)s %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger

logger = get_logger()


def validate_payload_json(payload: json) -> dict:
    try:
        # payload = json.loads(payload_str)
        raw_domain = payload.get('context', {}).get('domain', '')
        domain = raw_domain.split(":")[-1] if raw_domain else None # ONDC:RET10 -> RET10
        action = payload.get('context', {}).get('action', '')
        transaction_id = payload.get('context', {}).get('transaction_id', None)
        message_id = payload.get('context', {}).get('message_id', None)
        logger.debug(f"Validating payload | domain={domain}, action={action}, tx={transaction_id}, msg={message_id}")

        # Import validation module (cache)
        if domain not in validation_modules_cache:
            try:
                module_name = f"validations.{domain}.generated.l1_validations"
                logger.info(f"Loading validation module: {module_name}")
                validation_modules_cache[domain] = importlib.import_module(module_name)
            except ModuleNotFoundError:
                logger.warning(f"No validation module found for domain={domain}")
                return {
                    "status": "not_applicable",
                    "domain":payload['context'].get('domain', None),
                    "transaction_id": transaction_id,
                    "message_id": message_id,
                }

        l1_validations = validation_modules_cache[domain]
        result = l1_validations.perform_l1_validations(action, payload)
        logger.info(f"Validation success | domain={domain}, tx={transaction_id}")
        
        return {
            "status": "success",
            "result": result,
            "domain": raw_domain,
            "transaction_id": transaction_id,
            "message_id": message_id,
        }

    except Exception as e:
        logger.error(f"Validation failed: {str(e)}")
        return {
            "status": "error",
            "issues": [f"Validation error: {str(e)}"]
        }

@broker.subscriber(
    os.getenv("KAFKA_CONSUMER_TOPIC", "event-payloads"),
    group_id=os.getenv("KAFKA_CONSUMER_GROUP_ID", "validator-group"),
    max_poll_records=1,
    max_poll_interval_ms=120000,
    session_timeout_ms=30000
)
async def validate_event(event):
    handler_start = time.perf_counter()
    # payload = json.loads(event).get('data', {})
    payload = event.get('data', {})
    domain = payload.get("context", {}).get("domain", None)
    transaction_id = payload.get("context", {}).get('transaction_id', None)
    message_id = payload.get("context", {}).get('message_id', None)

    if domain not in domains_to_validate:
        logger.debug(f"Skipping validation | domain={domain}, tx={transaction_id}, msg={message_id}")
        result = {
                    "status": "not_applicable",
                    "domain": domain,
                    "transaction_id": transaction_id,
                    "message_id": message_id,
                }
    else:
        result = validate_payload_json(payload)
    
    total_elapsed_ms = (time.perf_counter() - handler_start) * 1000
    
    # calculate cloudwatch metrics
    payload_size = len(json.dumps(event).encode('utf-8'))
    payload_type = payload.get("context", {}).get("action", "unknown")

    logger.info("Publishing metrics to CloudWatch")

    cw_client.put_metric_data(
        Namespace='ondc-no/workbench',
        MetricData=[
            {
                'MetricName': 'ValidationProcessingTime',
                'Value': total_elapsed_ms,
                'Unit': 'Milliseconds',
                'Dimensions': [
                    {
                        'Name': 'Service',
                        'Value': 'json-validator'
                    },
                    {
                        'Name': 'Domain',
                        'Value': domain if domain else 'Unknown'
                    },
                    {
                        'Name': 'Status',
                        'Value': result.get("status", "unknown")
                    },
                    {
                        'Name': 'PayloadType',
                        'Value': payload_type
                    },
                ]
            },
            {
                'MetricName': 'PayloadSizeBytes',
                'Value': payload_size,
                'Unit': 'Bytes',
                'Dimensions': [
                    {
                        'Name': 'Service',
                        'Value': 'json-validator'
                    },
                    {
                        'Name': 'Domain',
                        'Value': domain if domain else 'Unknown'
                    },
                    {
                        'Name': 'Status',
                        'Value': result.get("status", "unknown")
                    },
                    {
                        'Name': 'PayloadType',
                        'Value': payload_type
                    },
                ]
            }
        ]
    )

    # logger.debug(f"Time taken for processing a payload: {total_elapsed_ms:.4f} ms | domain={domain}, tx={transaction_id}, msg={message_id}")

    if result.get("status") in ["success"]:
        await broker.publish(
                json.dumps(result)
                , topic=validation_success_topic
            )
    elif result.get("status") in ["not_applicable"]:
        await broker.publish(
                json.dumps(result)
                , topic=validation_missing_topic
            )

if __name__ == "__main__":
    asyncio.run(app.run())
