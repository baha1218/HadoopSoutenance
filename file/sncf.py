from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
from pyspark.sql.functions import col,struct,when, desc

spark = SparkSession \
    .builder \
    .appName("Read SNCF csv files") \
    .getOrCreate()

df = spark.read.load("sncf.csv", format="csv", sep=";", inferSchema="true", header="true")

result_df = df.limit(80)

result_df.show(80, 100, True)
result_df.write.mode("append").csv("/user/output", header=True)
