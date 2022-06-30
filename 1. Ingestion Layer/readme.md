# Ingestion Layer

The aim of this layer is to fetch the generated data and send each of it's record as a Kafka Message with a message producer.

***NB: this layer was designed with Python 3.10 in mind.***

***NB: an instance of redis-server must run in order for this layer to work.*** In order to do that [Redis](https://redis.io/download/) must be downloaded.
Once downloaded and installed, an instance of Redis server can simply be started by typing *redis-server* in your terminal.
If you want to check what's going under the hood, you can get all the keys with the command _'keys \*_'. If you already have other keys in your redis instance, a better
option would be _'keys \*(\*).\*'_. If you want to see the content of a specific key, the command _'get "**Key name**"'_ shold be issued. For multiple keys, the command _mget_
can be used. 

***NB: this layer requires an instance of Zookeeper and Apache Kafka Running***. Info for the download can be found at [Apache Kafka official website](https://kafka.apache.org/downloads).

In order to **start a Zookeeper instance**, the following command must be issued in the kafka installation folder (with a new terminal): *bin/zookeeper-server-start.sh config/zookeeper.properties*

In order to **start a Kafka broker instance**, the following command must be issued in the kafka installation folder (with a new terminal): *bin/kafka-server-start.sh config/server.properties*

If you want to manually create a topic (e.g. Bank topic), then the following command must be issued (on a new terminal): *bin/kafka-topics.sh --create --topic bank --bootstrap-server localhost:9092*

## Start the ingestion

The layer can be easily started by running the script 'main.py'.

The script will continuously fetch the documents' data from redis, unpack each row and send them individually as a kafka message, deleting the document from redis if the message was sent successfully.
With the script, topics are automatically created. 

The script is multithreaded and will start a thread for every producer (declaration,bank,broker and questura).