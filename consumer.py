from confluent_kafka import Consumer, KafkaException
import sys

conf = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "consumer-group-1",
    "session.timeout.ms": 6000,
    "auto.offset.reset": "earliest",
}

consumer = Consumer(conf)
consumer.subscribe(["test_topic"])

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        elif msg.error():
            raise KafkaException(msg.error())
        else:
            print(f"[{msg.topic()}][{msg.partition()}][{msg.offset()}]: {msg.value()}")

except Exception as e:
    print(f"Received exception while consuming: {e}")

finally:
    # Close down consumer to commit final offsets.
    consumer.close()
