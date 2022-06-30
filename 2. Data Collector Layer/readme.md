# Collector Layer

The aim of this layer is to fetch the categorized data from kafka and upload it to an object storage.

***NB: this layer was designed with Python 3.10 in mind.***

***NB: this layer requires an instance of Zookeeper and Apache Kafka Running***. Info for the download can be found at [Apache Kafka official website](https://kafka.apache.org/downloads).

In order to **start a Zookeeper instance**, the following command must be issued in the kafka installation folder (with a new terminal): *bin/zookeeper-server-start.sh config/zookeeper.properties*

In order to **start a Kafka broker instance**, the following command must be issued in the kafka installation folder (with a new terminal): *bin/kafka-server-start.sh config/server.properties*

If you want to **manually listen for a topic** (e.g. Bank topic), then the following command must be issued (on a new terminal): *bin/kafka-console-consumer.sh --topic bank --from-beginning --bootstrap-server localhost:9092*

***NB: this layer has been designed to work with Google Cloud Storage as an object storage***.

**In order for the script to work, a json credential file must be present into the "credentials" folder.**
The credential path can be changed in the file models/temp_storage_sender at line 13.

**The script does not create the buckets automatically**, they were created with the following logic: kafka_topic-bdt-13 *(e.g. bank-bdt-13)*.  The name can be changed at models/message_consumer.py, line 21.

If you wish to **delete all files sent into a bucket**, the following command must be issued in the Google Cloud shell: gsutil -m rm -r gs://bucket-name/\*


## Start the collection

The layer can be easily started by running the script 'main.py'.

The script will start a listener for each topic, read the messages and then send them to cloud storage into the buckets. If no messages are present, it will wait 60s before start listening again.

The script is multithreaded, a thread will be started for each consumer (statement, bank, broker, questura).