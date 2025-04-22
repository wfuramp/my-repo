from pyspark.ml.classification import LogisticRegressionModel

def run(spark, config):
    df = spark.read.format("bigquery").option("table", config["cleaned_table"]).load()

    model = LogisticRegressionModel.load(config["model_output_path"])
    result = model.transform(df)

    result.select("id", "prediction").write.format("bigquery") \
        .option("table", config["prediction_table"]) \
        .mode("overwrite") \
        .save()
