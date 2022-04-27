from pyspark.sql import SparkSession
import re

basePath = 'file:///poor-hdfs/'

spark = SparkSession.builder \
      .appName("wordcloud") \
      .master("spark://spark:7077") \
      .config("spark.jars", "/poor-hdfs/postgresql-42.3.4.jar") \
      .getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("ERROR")

txt = sc.textFile(basePath + 'uploads/*')
words = txt.flatMap(lambda line: re.split('\W+', line.lower()))
words = words.filter(lambda x: len(x) > 3)
wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)
sortedWordCounts = wordCounts.sortBy(lambda x: x[1])

output = sortedWordCounts.collect()
for (word, count) in output:
    print("%s: found %i times" % (word, count))

print("Number of different words -> %i" % (sortedWordCounts.count()))

# df = spark.createDataFrame(sortedWordCounts)
# df.write.jdbc("")

df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/postgres") \
    .option("dbtable", "word-cloud") \
    .option("user", "postgres") \
    .option("password", "passw0rd") \
    .option("driver", "org.postgresql.Driver") \
    .load()

df.printSchema()

sc.stop()
spark.stop()
