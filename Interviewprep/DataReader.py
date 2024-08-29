
from lib import ConfigReader

def get_sales_schema():
    schema="customer_id int,customer_fname string,customer_lname string,username string,password string,address string,city string,state string,pincode string"
    return schema

def read_customers(spark,env):
    conf=ConfigReader.get_app_config(env)
    customer_file_path=conf["sales.file.path"]
    return spark.read.format("csv").\
            option("header",True).\
            option("schema",get_sales_schema()).\
            load(customer_file_path)
