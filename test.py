from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Prq2csv").getOrCreate()
my_df = spark.read.parquet("userdata1.parquet")
my_df.toPandas().to_csv('my_new_file.csv', index=False)
# my_df.repartition(1).write.\
#     format("com.databricks.spark.csv").\
#     option("header", "true").\
#     save(path='my_latest.csv', mode='overwrite')

# emp_df.write.format('csv')\
#     .option('header','true')\
#     .save('s3a://pysparkcsvs3/pysparks3/emp_csv/emp.csv',mode='overwrite')

# from pyspark.sql.window import Window
#
# from pyspark.sql.functions import monotonically_increasing_id,row_number
#
# df =df.withColumn("row_idx",row_number().over(Window.orderBy(monotonically_increasing_id())))
