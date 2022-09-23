from confluent_kafka import Consumer, KafkaException
from transformers import pipeline
import json


def sentiment_analysis(msg, classifier):
    text = msg["text"]
    rating = msg["rating"]
    print(f"[{rating}] {text}")
    classified_msg = classifier(text)
    print(classified_msg)
    print()


def consume_loop(consumer, classifier):
    consumer.subscribe(["amazon_product_reviews"])
    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            elif msg.error():
                raise KafkaException(msg.error())
            else:
                json_msg = json.loads(msg.value().decode("utf-8"))
                # print(f"[{msg.topic()}][{msg.partition()}][{msg.offset()}]: {json_msg}")

                sentiment_analysis(json_msg, classifier)

    except Exception as e:
        print(f"Received exception while consuming: {e}")

    finally:
        # Close down consumer to commit final offsets.
        consumer.close()


conf = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "consumer-group-1",
    "session.timeout.ms": 6000,
    "auto.offset.reset": "earliest",
}

classifier = pipeline("sentiment-analysis")
consumer = Consumer(conf)
consume_loop(consumer, classifier)
