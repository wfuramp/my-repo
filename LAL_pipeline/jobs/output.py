def run(spark, config):
    df = spark.read.format("bigquery").option("table", config["prediction_table"]).load()
    df_final = df.withColumnRenamed("prediction", "predicted_label")

    df_final.write.format("bigquery") \
        .option("table", config["final_output_table"]) \
        .mode("overwrite") \
        .save()
