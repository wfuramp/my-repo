from pyspark.sql.functions import col
from utils.logger import setup_logger
from utils.retry import retry

logger = setup_logger("Pretreat")

@retry(attempts=3, interval_seconds=60, logger=logger)
def run(spark, config):
    try:
        logger.info("Start reading raw data from BigQuery.")
        df = spark.read.format("bigquery").option("table", config["bigquery"]["input_tables"]["raw"]).load()
        
        logger.info("Data successfully loaded, starting cleaning process.")
        df_clean = df.dropna().filter(col("price") > 0)

        logger.info("Cleaning successful, writing cleaned data to BigQuery.")
        df_clean.write.format("bigquery") \
            .option("table", config["bigquery"]["intermediate_tables"]["cleaned"]) \
            .mode("overwrite") \
            .save()

        logger.info("Cleaned data successfully written to BigQuery.")
    except Exception as e:
        logger.error(f"Error in pretreat.run: {e}")
        raise e
