# Ingestion Layer

The aim of this layer is to fetch the generated data and send each of it's record as a Kafka Message with a message producer.

***NB: this layer was designed with Python 3.10 in mind.***

***NB: an instance of a redis container must run in order for this layer to work.*** 
It can be instantiated with the following command: *docker run -d --name redis --network app-tier redis*


***NB: this layer requires an instance of Zookeeper and Apache Kafka Running***.
They can be both installed and initialized with the following commands:

*docker run -d --name zookeeper-server --network app-tier -e ALLOW_ANONYMOUS_LOGIN=yes bitnami/zookeeper:latest*

*docker run -d --name kafka-server --network app-tier -e ALLOW_PLAINTEXT_LISTENER=yes -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper-server:2181 bitnami/kafka:latest*


## Start the ingestion

The program can be started by:
1. building the image: *docker build -t bdt/ingestion-layer .*
2. starting the container: *docker run -d --name 1-Ingestion-Layer-BDT --network app-tier bdt/ingestion-layer*
