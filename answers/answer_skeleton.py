import os
from pyspark.sql import DataFrame
from pyspark.rdd import RDD
from pyspark.sql.functions import desc
from pyspark.sql import SparkSession
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql import Row
from pyspark.sql.functions import lit
import sys

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

def toCSVLineRDD(rdd):
    a = rdd.map(lambda row: ",".join([str(elt) for elt in row]))\
           .reduce(lambda x,y: "\n".join([x,y]))
    return a + "\n"
def toCSVLine(data):
    if isinstance(data, RDD):
        return toCSVLineRDD(data)
    elif isinstance(data, DataFrame):
        return toCSVLineRDD(data.rdd)
    return None

def basic_als_recommender(filename, seed):
    return 0

def global_average(filename, seed):
    return 0

def global_average_recommender(filename, seed):
    return 0

def means_and_interaction(filename, seed, n):
    return " bb"

def als_with_bias_recommender(filename, seed):
    return 0

