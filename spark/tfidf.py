from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
import re
import sys

basePath = 'file:///poor-hdfs/'

spark = SparkSession.builder \
      .appName("wordcloud") \
      .master("spark://spark:7077") \
      .getOrCreate()
      
sc = spark.sparkContext
sc.setLogLevel("ERROR")

filename=sys.argv[1]

txt = sc.textFile(basePath + 'uploads/' + filename)

# ['line one', ...] => [('word one', 1), ('word two', 1), ...]
words = txt.flatMap(lambda line: re.split('\W+', line.lower()))

# remove short / stop words
words = words.filter(lambda x: len(x) > 3)

# ['word one', 'word one', ...] => [('word one', 1), ('word one', 1), ...] => [('word one', 2)]
tf = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)

# TODO load df from database and calc tfidf

for i in tf.collect():
    print(i)

# sortedWordCounts = wordCounts.sortBy(lambda x: x[1])

schema = StructType([
        StructField('word', StringType(), False),
        StructField('amount', IntegerType(), False),
    ])

df = spark.createDataFrame(tf, schema=schema)

df.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/postgres") \
    .option("dbtable", "tfidf") \
    .option("user", "postgres") \
    .option("password", "passw0rd") \
    .option("truncate", True) \
    .save(mode="overwrite")

print("%i words have been saved to database" % (df.count()))

sc.stop()
spark.stop()
