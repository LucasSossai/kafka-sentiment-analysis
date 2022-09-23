from confluent_kafka.admin import AdminClient, NewTopic


admin_client = AdminClient({
    "bootstrap.servers": "localhost:9092"
})

topic_list = [NewTopic("amazon_product_reviews", 1, 1)]
ans = admin_client.create_topics(topic_list)
print(ans)
admin_client.list_topics()