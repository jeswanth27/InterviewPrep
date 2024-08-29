import configparser

from pyspark import SparkConf

def get_app_config(env):
    Config=configparser.ConfigParser()
    Config.read("configs/application.conf")
    app_config={}
    for (key,val) in Config.items(env):
        app_config[key]=val
    return app_config

def get_pyspark_config(env):
    Config=configparser.ConfigParser()
    Config.read("configs/Pyspark.conf")
    pysparkconf=SparkConf()
    for (key,val) in Config.items(env):
        pysparkconf.set(key,val)
    return pysparkconf
