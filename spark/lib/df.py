from pyspark.sql import SparkSession

def get_df(spark: SparkSession):
    df = spark.sparkContext.parallelize([])

    try:
        df = spark.read \
            .format("jdbc") \
            .option("url", "jdbc:postgresql://postgres:5432/postgres") \
            .option("dbtable", "df") \
            .option("user", "postgres") \
            .option("password", "passw0rd") \
            .load().rdd()
    except:
        print("Database could not be loaded (probably not existing)")

    return df  
