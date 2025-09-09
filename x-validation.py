from pyspark.sql import SparkSession, Row
# Row above is only required for creating parquet row
from pyspark.sql.functions import col, explode, from_json, udf
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, LongType
import json
import sys

from validations.RET10.generated import l1_validations
# read json data from the raw json payloads
def read_json_data(spark, paths):
    # json root fields are type, user_id, data
    schema = StructType([
        StructField("type", StringType(), True),
        StructField("user_id", StringType(), True),
        StructField("data", StringType(), True),
        # server-timestamp long type
        StructField("server-timestamp", LongType(), True),
    ])
    # since paths can be directory, we need to read them seperately and union them
    raw_df = None
    for path in paths:
        print(path)
        json_raw_df_single = spark.read.schema(schema).json(path)
        if raw_df is None:
            raw_df = json_raw_df_single
        else:
            raw_df = raw_df.union(json_raw_df_single)
    # rename data to value
    json_raw_df = raw_df.withColumnRenamed("data", "value")
    # json_raw_df.show()
    return json_raw_df


# UDF wrapper (returns JSON string)
def validate_payload_json(payload_str:str)->str:
    try:
        payload = json.loads(payload_str)
        result = l1_validations.perform_l1_validations(payload['context']['action'],payload)  # validation compiler 
        return json.dumps(result)
    except Exception as e:
        return json.dumps({"issues": [f"Validation error: {str(e)}"]})

validate_udf = udf(validate_payload_json, StringType())


def output_to_csv(df, output_path):
    df.write.mode("overwrite").csv(output_path, header=True)

def run_validation(df):
    df.show(3)
    return (
        df.withColumn("validation", validate_udf(col("value")))
          .select("user_id", "type", "validation")
    )

# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("ONDC Payload Validation") \
        .enableHiveSupport() \
        .getOrCreate()
    json_raw_df= read_json_data(spark, ["events+0+3073386206.bin"])

    output_df=run_validation(json_raw_df)
    output_df.show(2)
    output_to_csv(output_df, "output")
    

    spark.stop()