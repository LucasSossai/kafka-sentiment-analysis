from confluent_kafka import Producer
import time
import pandas as pd


def acked(err, msg):
    if err is not None:
        print(f"Failed to deliver message: {str(msg)}: {str(err)}")
    else:
        print(f"[{msg.offset()}-{msg.topic()}]: {msg.value()}")


def produce_meessages(producer, topic, data_path):
    df = pd.read_csv(data_path)
    for index, row in df.iterrows():
        message = row.to_json()
        producer.produce(topic, message, callback=acked)
        producer.poll(0)
        time.sleep(1)


conf = {"bootstrap.servers": "localhost:9092", "client.id": "producer"}
producer = Producer(conf)
produce_meessages(producer, "amazon_product_reviews", "data/clean_data.csv")
