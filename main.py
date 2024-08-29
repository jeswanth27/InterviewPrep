import json
import time

from confluent_kafka import Producer

conf={'bootstrap.servers':'pkc-12576z.us-west2.gcp.confluent.cloud:9092',
      'security.protocol':'SASL_SSL',
      'sasl.mechanism':'PLAIN',
      'sasl.username':'UMBV46H3WHIEIEPD',
      'sasl.password':'PjLknn5cFTiqJjKGZXBHj3BoF+kLS4002M1Vg8ecE2mcNd3hFoHo6meZIRHUTEXs',
      'client.id':'jeswanth'}

producer=Producer(conf)

#cust_id='267'
#cust_value='{"order_id":1,"customer_id":11599,"customer_fname":"Mary","customer_lname":"Malone","city":"Hickory","state":"NC","pincode":28601,"line_items":[{"order_item_id":1,"order_item_product_id":957,"order_item_quantity":1,"order_item_product_price":299.98,"order_item_subtotal":299.98}]}'

def ack(err,msg):
    if err is not None:
        print("failed to deliver: %S %S"%(str(msg),str(err)))
    else:
        msg_key=msg.key().decode("utf-8")
        msg_value=msg.value().decode("utf-8")

        print(f"message produced key is {msg_key} and value {msg_value}")

with open("C:/Users/DELL\OneDrive\Desktop\Bigdata\Week 29 kafka\order_input.json",'r') as file:
    for line in file:
        order=json.loads(line)
        cust_id=str(order["customer_id"])
        producer.produce("orders_raw_data", key=cust_id, value=line, callback=ack)
        producer.poll(1)
        producer.flush()
        time.sleep(5)




