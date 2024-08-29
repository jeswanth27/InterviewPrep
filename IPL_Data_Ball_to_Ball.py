import json
import csv
import time
import hashlib

from confluent_kafka import Producer

class CustomPartitioner(Producer):
    def __init__(self, config):
        super().__init__(config)

    def partition(self, topic, key, partition_count):
        # Custom hash-based partitioning
        if key is None:
            return 0  # If key is None, assign to partition 0
        key_bytes = key.encode('utf-8')
        key_hash = int(hashlib.md5(key_bytes).hexdigest(), 16)
        return key_hash % partition_count  # Hash-based partitioning


conf={'bootstrap.servers':'pkc-12576z.us-west2.gcp.confluent.cloud:9092',
      'security.protocol':'SASL_SSL',
      'sasl.mechanism':'PLAIN',
      'sasl.username':'X4ANKR4O3J3NBUTH',
      'sasl.password':'crUT5VWaKeLIHwyaLsg2k6w2rMswzJgPEbv0Az4mpTRGC4AbAMpcFwcE3kUPizMF',
      'client.id':'jeswanth'}

#producer=Producer(conf)
producer = CustomPartitioner(conf)

#cust_id='267'
#cust_value='{"order_id":1,"customer_id":11599,"customer_fname":"Mary","customer_lname":"Malone","city":"Hickory","state":"NC","pincode":28601,"line_items":[{"order_item_id":1,"order_item_product_id":957,"order_item_quantity":1,"order_item_product_price":299.98,"order_item_subtotal":299.98}]}'

def ack(err,msg):
    if err is not None:
        print("failed to deliver: %S %S"%(str(msg),str(err)))
    else:
        msg_key=msg.key().decode("utf-8")
        msg_value=msg.value().decode("utf-8")

        print(f"message produced key is {msg_key} and value {msg_value}")

with open("C:/Users/DELL/OneDrive/Desktop/Bigdata/IPL_Datasets/raghu543-ipl-data-till-2017/raghu543-ipl-data-till-2017/Ball_to_Ball_2017_2.csv",
        'r') as file:
    # Create a CSV reader object
    reader = csv.DictReader(file)
    # Iterate over the rows in the CSV file
    for row in reader:
        # Convert the row to JSON string
        line = json.dumps(row)
        # Extract the customer_id
        match_id = str(row["Match_id"])
        # Produce the message to Kafka
        producer.produce("ball_to_ball", key=match_id, value=line, callback=ack)
        # Poll to handle delivery reports
        producer.poll(1)
        # Flush the producer to make sure all messages are sent
        producer.flush()
        # Sleep for 5 seconds
        time.sleep(5)




