# Cloud y Big Data
# Realizado por Jorge Rosello, Daniel Alcazar, Francisco Javier Lozano
# Nombre Script: S7
# Descripcion: Extrae el numero de posts nsfw de cada subreddit.

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pushshift import file_to_dataframe

conf = SparkConf().setAppName('S7')
sc = SparkContext(conf=conf)
ss = SparkSession(sc)
df = file_to_dataframe('RS_2019-01', ss)

df.filter(col("over_18") == True)\
    .groupBy(col("subreddit")).count().\
    select("subreddit", col("count").alias("nsfw_posts")).write.json("s7_salida")