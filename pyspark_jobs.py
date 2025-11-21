"""
%idle_timeout 2880
%glue_version 5.0
%worker_type G.1X
%number_of_workers 3
# validation is present  s3://ondc-rds-analytics-data-export/pyspark/validations.zip
%extra_py_files s3://ondc-rds-analytics-data-export/pyspark/validations.zip
"""

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession
from datetime import datetime
from pyspark.sql.functions import col, udf, from_json, split, lit
from pyspark.sql.types import StructType, StructField, StringType, LongType, ArrayType
import json
import importlib

# --------------------------------------------------------
# Initialize Glue Context
# --------------------------------------------------------
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# --------------------------------------------------------
# Validation with caching
# --------------------------------------------------------
validation_modules_cache = {}


def validate_payload_json(payload_str: str) -> str:
    try:
        payload = json.loads(payload_str)
        raw_domain = payload['context'].get('domain', '')
        domain = raw_domain.split(":")[-1] if raw_domain else None  # ONDC:RET10 -> RET10
        action = payload['context'].get('action', '')
        transaction_id = payload['context'].get('transaction_id', None)
        message_id = payload['context'].get('message_id', None)
        print(f"[DEBUG] Validating payload | domain={domain}, action={action}, tx={transaction_id}, msg={message_id}")

        # Import validation module (cache)
        if domain not in validation_modules_cache:
            try:
                module_name = f"validations.{domain}.generated.l1_validations"
                print(f"[INFO] Loading validation module: {module_name}")
                validation_modules_cache[domain] = importlib.import_module(module_name)
            except ModuleNotFoundError:
                print(f"[WARN] No validation module found for domain={domain}")
                print("unable to load the modules")
                return json.dumps({
                    "status": "not_applicable",
                    "domain": payload['context'].get('domain', None),
                    "transaction_id": transaction_id,
                    "message_id": message_id,
                })

        l1_validations = validation_modules_cache[domain]
        result = l1_validations.perform_l1_validations(action, payload)
        print(f"[INFO] Validation success | domain={domain}, tx={transaction_id}")
        return json.dumps({
            "status": "success",
            "result": result,
            "domain": payload['context'].get('domain', None),
            "transaction_id": transaction_id,
            "message_id": message_id,
        })

    except Exception as e:
        print(f"[ERROR] Validation failed: {str(e)}")
        return json.dumps({
            "status": "error",
            "issues": [f"Validation error: {str(e)}"]
        })


validate_udf = udf(validate_payload_json, StringType())


# --------------------------------------------------------
# IO Helpers
# --------------------------------------------------------
def read_parquet_data(spark, paths):
    """
    Read parquet files containing 'data' column with JSON payload
    Assumes parquet already has 'domain' column for filtering
    """
    raw_df = None
    for path in paths:
        print(f"[INFO] Reading input parquet path: {path}")
        df_single = spark.read.parquet(path)
        raw_df = df_single if raw_df is None else raw_df.union(df_single)

    record_count = raw_df.count()
    print(f"[INFO] Finished reading input files. Total records: {record_count}")
    return raw_df


def output_to_parquet(df, base_path):
    today = datetime.now().strftime("%Y-%m-%d")
    df_with_date = df.withColumn("dt", lit(today))  # add partition column
    print(f"[INFO] Writing DataFrame to {base_path} partitioned by dt={today}")
    (
        df_with_date.write
        .mode("append")  # append data if partition exists
        .partitionBy("dt")  # creates dt=YYYY-MM-DD folders
        .parquet(base_path)
    )
    print(f"[INFO] Write complete (in parquet): {base_path}")


# --------------------------------------------------------
# Main validation runner with domain filtering
# --------------------------------------------------------
def run_validation(df, target_domains=None):
    """
    Run validation with domain filtering applied before UDF execution

    Args:
        df: Input DataFrame with 'data' column containing JSON payload and 'domain' column
        target_domains: List of domains to process (e.g., ['RET10', 'RET11']).
                       If None, process all domains.
    """
    print("[INFO] Using existing domain column for filtering...")

    # Show domain distribution
    print("[INFO] Domain distribution in dataset:")
    df.groupBy("domain").count().orderBy("domain").show(50, truncate=False)

    # Apply domain filter if specified
    if target_domains:
        print(f"[INFO] Filtering for domains: {target_domains}")
        df_filtered = df.filter(col("domain").isin(target_domains))
        filtered_count = df_filtered.count()
        print(f"[INFO] Records after domain filtering: {filtered_count}")

        if filtered_count == 0:
            print("[WARN] No records found for specified domains!")
            return None, None
    else:
        print("[INFO] Processing all domains")
        df_filtered = df

    # Rename 'data' column to 'value' for compatibility with validation UDF
    df_enriched = df_filtered.withColumnRenamed("data", "value")

    print("[INFO] Running validation UDF...")
    df_validated = df_enriched.withColumn("validation", validate_udf(col("value")))
    print("[INFO] Parsing validation results into structured columns...")

    # Parse JSON result into columns
    df_parsed = df_validated.withColumn("parsed", from_json(col("validation"),
                                                            StructType([
                                                                StructField("status", StringType(), True),
                                                                StructField("transaction_id", StringType(), True),
                                                                StructField("message_id", StringType(), True),
                                                                StructField("issues", ArrayType(StringType()), True),
                                                                StructField("result", StringType(), True),
                                                                StructField("domain", StringType(), True),
                                                            ])
                                                            )).withColumn("subscriber_id",
                                                                          split(col("user_id"), "@")[0]).withColumn(
        "subscriber_type", split(col("user_id"), "@")[1])

    base_cols = [
        col("subscriber_id"),
        col("parsed.domain"),
        col("type").alias("API"),
        col("parsed.transaction_id"),
        col("parsed.message_id"),
        col("subscriber_type")
    ]

    print("[INFO] Filtering validations Performed...")
    # Separate outputs
    df_success = df_parsed.filter(col("parsed.status") == "success").select(*base_cols,
                                                                            col("parsed.result").alias("issues"))

    print("[INFO] Filtering validations not applicable...")
    df_missing = df_parsed.filter(col("parsed.status") == "not_applicable").select(*base_cols)

    print("[INFO] Validation pipeline completed")
    success_count = df_success.count()
    missing_count = df_missing.count()
    print(f"[INFO] Success count: {success_count}")
    print(f"[INFO] Not applicable count: {missing_count}")

    return df_success, df_missing


# --------------------------------------------------------
# Main Execution
# --------------------------------------------------------
print("[START] AWS Glue Job: ONDC Payload Validation from Parquet")

# Input paths - Update with your parquet paths
input_paths = [
    "s3://ondc-rds-analytics-data-export/parquet-data/dt=2024-08-15/",
    # Add more paths as needed
]

# Read parquet data (assumes columns: data, domain, type, user_id)
parquet_df = read_parquet_data(spark, input_paths)

# Specify target domains to filter (or None for all domains)
# Example: target_domains = ['RET10', 'RET11', 'RET12']
# Set to None to process all domains
target_domains = ['RET10']  # Change this based on your needs

# Run validation with domain filtering
df_success, df_missing = run_validation(parquet_df, target_domains=target_domains)

if df_success is not None and df_missing is not None:
    # Write outputs
    print("[INFO] Showing dataframes where validations are performed...")
    df_success.show(2, truncate=False)

    print("[INFO] Showing dataframes where validations are not applicable...")
    df_missing.show(2, truncate=False)

    output_to_parquet(
        df_success,
        "s3://ondc-rds-analytics-data-export/temp/pyspark-validations-job/output/validations_done"
    )
    output_to_parquet(
        df_missing,
        "s3://ondc-rds-analytics-data-export/temp/pyspark-validations-job/output/validations_missing"
    )

    print("[SUCCESS] Job completed successfully")
else:
    print("[ERROR] No data to process after filtering")

# Commit the Glue job
job.commit()