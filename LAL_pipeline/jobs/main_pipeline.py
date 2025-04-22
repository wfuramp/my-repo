from utils.config_utils import load_config
from utils.spark_utils import get_spark_session
from utils.logger import setup_logger
import jobs.pretreat as pretreat
import jobs.train_model as train_model
import jobs.predict as predict
import jobs.output as output

def main():
    logger = setup_logger("MainPipeline")
    config = load_config("configs/pipeline_config.yaml")
    spark = get_spark_session("FullPipeline")

    try:
        logger.info("Pipeline execution started.")

        pretreat.run(spark, config)
        train_model.run(spark, config)
        predict.run(spark, config)
        output.run(spark, config)

        logger.info("Pipeline execution completed successfully.")
    except Exception as e:
        logger.error(f"Pipeline execution failed: {e}")
    finally:
        spark.stop()

if __name__ == "__main__":
    main()
