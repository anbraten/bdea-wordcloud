from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, FloatType
import re
import os
import math

basePath = 'file:///poor-hdfs/'

spark = SparkSession.builder \
      .appName("wordcloud") \
      .master("spark://spark:7077") \
      .getOrCreate()
      
sc = spark.sparkContext
sc.setLogLevel("ERROR")

txt = sc.wholeTextFiles(basePath + 'uploads/*.txt')

txtAmount = txt.count()
print("%i files will be scanned ..." % (txtAmount))

# [('path to file', 'content of the file')] => [(('filename', 'lower case word'), 1)]
words = txt.flatMap(lambda x: [((os.path.basename(x[0]),i.lower()),1) for i in re.split('\W+', x[1])])

# remove short / stop words
words = words.filter(lambda x: len(x[0][1]) > 3)

# [(('filename', 'lower case word'), 1), (('filename', 'lower case word'), 1)] => [(('filename', 'lower case word'), 2)]
words = words.reduceByKey(lambda x,y:x+y)

# [(('filename', 'lower case word'), 2)] => [('lower case word', ('filename', 2))]
tf = words.map(lambda x: (x[0][1],(x[0][0],x[1])))

df = tf.map(lambda x: (x[0],1)).reduceByKey(lambda x,y:x+y)

df = df.map(lambda x: (x[0], math.log10(txtAmount / x[1])))

# for i in df.collect():
#     print(i)

# sortedWordCounts = wordCounts.sortBy(lambda x: x[1])

schema = StructType([
        StructField('word', StringType(), False),
        StructField('idf', FloatType(), False),
    ])

df = spark.createDataFrame(df, schema=schema)

df.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/postgres") \
    .option("dbtable", "df") \
    .option("user", "postgres") \
    .option("password", "passw0rd") \
    .option("truncate", True) \
    .save(mode="overwrite")

print("%i words have been saved to database" % (df.count()))

sc.stop()
spark.stop()
