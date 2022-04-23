from pyspark.sql import SparkSession
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
# sortedWordCounts.saveAsTextFile(basePath + "/output/")

output = sortedWordCounts.collect()
for (word, count) in output:
    print("%s: found %i times" % (word, count))

print("Number of different words -> %i" % (sortedWordCounts.count()))

sc.stop()
spark.stop()
