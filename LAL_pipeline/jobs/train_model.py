from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
import shutil

def run(spark, config):
    df = spark.read.format("bigquery").option("table", config["cleaned_table"]).load()
    df = df.withColumnRenamed("label", "target")  # 假设你有label列

    assembler = VectorAssembler(inputCols=[col for col in df.columns if col not in ["target"]], outputCol="features")
    df_vec = assembler.transform(df).select("features", "target")

    lr = LogisticRegression(featuresCol="features", labelCol="target")
    model = lr.fit(df_vec)

    model.write().overwrite().save(config["model_output_path"])
