from faststream import FastStream
from faststream.kafka import KafkaBroker
from pydantic import BaseModel
import json
import importlib
import asyncio
from dotenv import load_dotenv
import os
import time

load_dotenv(dotenv_path = '.env')

broker = KafkaBroker(os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"))
app = FastStream(broker)

validation_modules_cache = {}
domains_to_validate = [os.getenv("DOMAIN_TO_VALIDATE", "ONDC:RET10")]

def validate_payload_json(payload: json) -> dict:
    try:
        # payload = json.loads(payload_str)
        raw_domain = payload.get('context', {}).get('domain', '')
        domain = raw_domain.split(":")[-1] if raw_domain else None # ONDC:RET10 -> RET10
        action = payload.get('context', {}).get('action', '')
        transaction_id = payload.get('context', {}).get('transaction_id', None)
        message_id = payload.get('context', {}).get('message_id', None)
        print(f"[DEBUG] Validating payload | domain={domain}, action={action}, tx={transaction_id}, msg={message_id}")

        # Import validation module (cache)
        if domain not in validation_modules_cache:
            try:
                module_name = f"validations.{domain}.generated.l1_validations"
                print(f"[INFO] Loading validation module: {module_name}")
                validation_modules_cache[domain] = importlib.import_module(module_name)
            except ModuleNotFoundError:
                print(f"[WARN] No validation module found for domain={domain}")
                return {
                    "status": "not_applicable",
                    "domain":payload['context'].get('domain', None),
                    "transaction_id": transaction_id,
                    "message_id": message_id,
                }

        l1_validations = validation_modules_cache[domain]
        result = l1_validations.perform_l1_validations(action, payload)
        print(f"[INFO] Validation success | domain={domain}, tx={transaction_id}")
        return {
            "status": "success",
            "result": result,
            "domain": raw_domain,
            "transaction_id": transaction_id,
            "message_id": message_id,
        }

    except Exception as e:
        print(f"[ERROR] Validation failed: {str(e)}")
        return {
            "status": "error",
            "issues": [f"Validation error: {str(e)}"]
        }

@broker.subscriber(
    os.getenv("KAFKA_CONSUMER_TOPIC", "event-payloads"),
    group_id=os.getenv("KAFKA_CONSUMER_GROUP_ID", "validator-group"),
)
async def validate_event(event):
    handler_start = time.perf_counter()
    payload = json.loads(event).get('data', {})
    domain = payload.get("context", {}).get("domain", None)
    transaction_id = payload.get("context", {}).get('transaction_id', None)
    message_id = payload.get("context", {}).get('message_id', None)

    if domain not in domains_to_validate:
        print(f"[DEBUG] Skipping validation | domain={domain}, tx={transaction_id}, msg={message_id}")
        result = {
                    "status": "not_applicable",
                    "domain": domain,
                    "transaction_id": transaction_id,
                    "message_id": message_id,
                }
    else:
        result = validate_payload_json(payload)
    
    total_elapsed_ms = (time.perf_counter() - handler_start) * 1000
    print(f"[DEBUG] Time taken for processing a payload: {total_elapsed_ms:.4f} ms | domain={domain}, tx={transaction_id}, msg={message_id}")

    if result.get("status") in ["success"]:
        await broker.publish(
                json.dumps(result)
                , topic="validations-done"
            )
    elif result.get("status") in ["not_applicable"]:
        await broker.publish(
                json.dumps(result)
                , topic="validations-missing"
            )

if __name__ == "__main__":
    asyncio.run(app.run())
