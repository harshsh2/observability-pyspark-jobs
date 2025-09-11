from pyspark.sql import SparkSession
from datetime import datetime
from pyspark.sql.functions import col, udf, from_json, split, lit
from pyspark.sql.types import StructType, StructField, StringType, LongType, ArrayType
import json
import importlib

# --------------------------------------------------------
# Schema for raw payload
# --------------------------------------------------------
schema = StructType([
    StructField("type", StringType(), True),
    StructField("user_id", StringType(), True),
    StructField("data", StringType(), True),   # raw JSON string
    StructField("server-timestamp", LongType(), True),
])

# --------------------------------------------------------
# Validation with caching
# --------------------------------------------------------
validation_modules_cache = {}

def validate_payload_json(payload_str: str) -> str:
    try:
        payload = json.loads(payload_str)
        raw_domain = payload['context'].get('domain', '')
        domain = raw_domain.split(":")[-1] if raw_domain else None # ONDC:RET10 -> RET10
        action = payload['context'].get('action', '')
        transaction_id= payload['context'].get('transaction_id', None)
        message_id= payload['context'].get('message_id', None),

        # Import validation module (cache)
        if domain not in validation_modules_cache:
            try:
                module_name = f"validations.{domain}.generated.l1_validations"
                validation_modules_cache[domain] = importlib.import_module(module_name)
            except ModuleNotFoundError:
                return json.dumps({
                    "status": "not_applicable",
                    "domain":payload['context'].get('domain', None),
                    "transaction_id": transaction_id,
                    "message_id": message_id,
                })

        l1_validations = validation_modules_cache[domain]
        result = l1_validations.perform_l1_validations(action, payload)
        return json.dumps({
            "status": "success",
            "result": result,
            "domain":payload['context'].get('domain', None),
            "transaction_id": transaction_id,
            "message_id": message_id,
        })

    except Exception as e:
        return json.dumps({
            "status": "error",
            "issues": [f"Validation error: {str(e)}"]
        })

validate_udf = udf(validate_payload_json, StringType())

# --------------------------------------------------------
# IO Helpers
# --------------------------------------------------------
def read_json_data(spark, paths):
    raw_df = None
    for path in paths:
        print(f"Reading: {path}")
        df_single = spark.read.schema(schema).json(path)
        raw_df = df_single if raw_df is None else raw_df.union(df_single)
    return raw_df.withColumnRenamed("data", "value")

# def output_to_parquet(df, output_path):
#     df.write.mode("overwrite").parquet(output_path)

def output_to_parquet(df, base_path):
    today = datetime.now().strftime("%Y-%m-%d")
    df_with_date = df.withColumn("dt", lit(today))  # add partition column

    (
        df_with_date.write
        .mode("append")         # append data if partition exists
        .partitionBy("dt")      # creates dt=YYYY-MM-DD folders
        .parquet(base_path)
    )
# --------------------------------------------------------
# Main validation runner
# --------------------------------------------------------
def run_validation(df):
    df_validated = df.withColumn("validation", validate_udf(col("value")))

    # parse JSON result into columns
    df_parsed = df_validated.withColumn("parsed", from_json(col("validation"), 
        StructType([
            StructField("status", StringType(), True),
            StructField("transaction_id", StringType(), True),
            StructField("message_id", StringType(), True),
            StructField("issues", ArrayType(StringType()), True),
            StructField("result", StringType(), True),
            StructField("domain", StringType(), True),
        ])
    )).withColumn("subscriber_id", split(col("user_id"), "@")[0]).withColumn("subscriber_type", split(col("user_id"), "@")[1])


    base_cols = [
        col("subscriber_id"),
        col("parsed.domain"),
        col("type").alias("API"),
        col("parsed.transaction_id"),
        col("parsed.message_id"),
        col("subscriber_type")
    ]

    # separate outputs
    df_success = df_parsed.filter(col("parsed.status") == "success").select(*base_cols,
        col("parsed.result").alias("issues"))

    df_missing = df_parsed.filter(col("parsed.status") == "not_applicable").select(*base_cols)

    return df_success, df_missing

# --------------------------------------------------------
# Main
# --------------------------------------------------------
if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("ONDC Payload Validation") \
        .enableHiveSupport() \
        .getOrCreate()

    # Input
    json_raw_df = read_json_data(spark, ["events+0+3073386206.bin"])

    # Run validation
    df_success, df_missing = run_validation(json_raw_df)
    # Write outputs
    df_success.show(2)
    df_missing.show(2)
    output_to_parquet(df_success, "output/validations_done")
    output_to_parquet(df_missing, "output/validations_missing")

    spark.stop()