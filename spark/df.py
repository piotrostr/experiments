#!/bin/env python3

from pyspark.sql import SparkSession


if __name__ == "__main__":
    spark = SparkSession.builder.appName("experiment").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")
    df = spark.read.csv("./melb_data.csv", header=True, inferSchema=True)
    df.show()
    pdf = df.pandas_api()
    pdf.head()

