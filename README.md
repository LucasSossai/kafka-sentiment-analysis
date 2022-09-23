# kafka-sentiment-analysis

Example of real-time sentiment analysis service using Kafka, a pre-trained NLP model, and an Amazon Reviews dataset from Kaggle.

Dataset: [Amazon Reviews Sentiment Analysis](https://www.kaggle.com/code/lele1995/amazon-reviews-sentiment-analysis/notebook).

## Requirements

* docker-compose
* python
* install requirements.txt python libs

## Steps

* Setup the localstack using docker-compose up -d command at localstack folder
* Download the dataset from kaggle and put the file 1429_1.csv at data folder
* Run the clean_data.py script to generate the clean_data.csv file
* Run the admin.py script to create the kafka topics
* Open one terminal and run the producer.py script to start producing messages
* Open another terminal and execute the consumer.py script to start consuming messages

You should start seeing the results at the consumer terminal.
