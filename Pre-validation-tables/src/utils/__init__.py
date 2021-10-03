from pyspark import SparkContext, SparkConf
from src.utils.loggin_messages import error_messages, info_messages

def init_spark_config(app_name, master="local"):
    conf = SparkConf().setAppName(app_name).setMaster(master)
    return SparkContext(conf = conf)