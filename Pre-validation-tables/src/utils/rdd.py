from . import init_spark_config
from pyspark.sql import SQLContext


def create_spark(pd_dataframe, app_name):
    spark_context = init_spark_config(app_name)
    sqlContext = SQLContext(spark_context)
    return sqlContext.createDataFrame(pd_dataframe)