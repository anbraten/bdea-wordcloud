from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
import re

basePath = 'file:///poor-hdfs/'

spark = SparkSession.builder \
      .appName("wordcloud") \
      .master("spark://spark:7077") \
      .getOrCreate()
      
sc = spark.sparkContext
sc.setLogLevel("ERROR")

txt = sc.textFile(basePath + 'uploads/*')
words = txt.flatMap(lambda line: re.split('\W+', line.lower()))
words = words.filter(lambda x: len(x) > 3)
wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)
sortedWordCounts = wordCounts.sortBy(lambda x: x[1])

output = sortedWordCounts.collect()
# for (word, count) in output:
#     print("%s: found %i times" % (word, count))

schema = StructType([
        StructField('word', StringType(), False),
        StructField('amount', IntegerType(), False),
    ])

df = spark.createDataFrame(sortedWordCounts, schema=schema)

df.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/postgres") \
    .option("dbtable", "wordcloud") \
    .option("user", "postgres") \
    .option("password", "passw0rd") \
    .option("truncate", True) \
    .save(mode="append")

print("%i words have been saved to database" % (sortedWordCounts.count()))

sc.stop()
spark.stop()
