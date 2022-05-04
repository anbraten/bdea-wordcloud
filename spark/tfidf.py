from pyspark.sql import SparkSession
import re
import sys
import math
import os.path
from lib.wordcloud import generate_wordcloud
from lib.df import get_df

spark = SparkSession.builder \
      .appName("wordcloud") \
      .master("spark://spark:7077") \
      .getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("ERROR")

basePath = '/fake-hdfs/'
filename=sys.argv[1]
filepath=os.path.join(basePath, 'uploads', filename)
svgFile=os.path.join(basePath, 'wordclouds', filename.replace('.txt', '.svg'))

txt = sc.textFile('file://'+filepath)

# SOURCE: https://towardsdatascience.com/tf-idf-calculation-using-map-reduce-algorithm-in-pyspark-e89b5758e64c

# ['line one', ...] => [('word one', 1), ('word two', 1), ...]
words = txt.flatMap(lambda line: re.split('\W+', line.lower()))

# remove short / stop words
words = words.filter(lambda x: len(x) > 3)

# ['word one', 'word one', ...] => [('word one', 1), ('word one', 1), ...] => [('word one', 2)]
tf = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)

df = get_df(spark)

# left join and set df to 1 if it is None
tfidf = tf.leftOuterJoin(df).map(lambda x: (x[0], (x[1][0], x[1][1] or 1)))
tfidf = tfidf.map(lambda x: (x[0], x[1][0] * x[1][1]))
tfidf = tfidf.map(lambda x: (x[0], math.ceil(x[1])))

generate_wordcloud(svgFile, dict(tfidf.collect()))

print("%i words have been saved to wordcloud" % (tfidf.count()))

sc.stop()
spark.stop()
