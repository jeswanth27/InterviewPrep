from pyspark.sql.functions import *
from Utils import get_spark_session
import DataReader

if __name__=="__main__":
    if len(sys.argv)<2:
        print("please specify environment")
        exit(1)

    job_run_env=sys.argv[1]
    print("create spark session")
    spark=get_spark_session(job_run_env)
    print(f"Application Id: {spark.sparkContext.applicationId}")
    print("create customer dataframe main")
    df=DataReader.read_customers(spark,job_run_env)
    df.show()
    exit(0)