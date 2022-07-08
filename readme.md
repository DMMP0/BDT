# Big Data Technologies Project: FISCO

The scope of this project was to design and implement a big data system that can provide credit scoring for companies that are not mandated to deposit a balance sheet (e.g., partnerships).

Each folder of the project corresponds to a step in the pipeline and is intended to run separately.
A script has been provided to run all the layers.

Every step has been divided in three folders:
1. Components, where the work not related to classes or data transportation is done;
2. Model, where all the classes are located;
3. Services, which aim is to handle data transportation between technologies;

This branch of the project works with docker in mind, for a local solution please refer to the branch _"main"_.

This project is licensed with the *GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007*, for more information please refer to the file **COPYING**.

Below lies a brief description of what each layer does, for a more detailed explanation consult the readme of each folder.

***Required containers (whole pipeline)***:
+ Python (the whole project was designed tested with Python 3.10 in mind);
+ Redis;
+ Zookeeper;
+ Apache Kafka;
+ MySQL 

the credentials for Google Cloud Storage and MySQL must be passed as environment variables.

***NB: a driver bridge must be created in order to allow the containers to speak together***
On can be created with the following command: *docker network create app-tier --driver bridge*


## 0. Source Layer

The aim of the source layer is to generate and categorize data.
All documents are generated in the folder "components/reports".
They are later parsed into json format and sent into a temporary storage (Redis).

***An instance of Redis container called 'redis' must run for this layer to work if you are not going to modify the code.***

## 1. Ingestion Layer

The aim of the ingestion layer is to fetch the parsed data, categorize and divide it.
A Kafka message producer will extract the data from Redis and divide it into topics before sending it.

***An instance of Zookeeper and Apache Kafka containers must run for this layer to work. Kafka container should be called 'kafka-server' if you are not going to modify the code. ***

## 2. Data Collector Layer

This layer will read the messages with a Kafka Listener and based on the topic it will upload them into an object storage bucket.

***An instance of Zookeeper and Apache Kafka must run for this layer to work. Kafka container should be called 'kafka-server' if you are not going to modify the code***

## 3. Data processing Layer

This layer will fetch the records from the object storage, cleaning and preparing them for the database insertion.

***An instance of Redis container called 'redis' must run for this layer to work  if you are not going to modify the code.***

## 4. Data Storage Layer 

This layer will fetch the prepared data from redis and insert it into an SQL database.


***An instance of Redis container called 'redis' must run for this layer to work, if you are not going to modify the code.***

***An instance of a mysql container called 'mysql' also must run for this layer to work, if you are not going to modify the code.***

## 5. Query Layer

This layer will act as a broker between the front-end and the back-end of the application.

***An instance of a mysql container called 'mysql' also must run for this layer to work, if you are not going to modify the code.***
