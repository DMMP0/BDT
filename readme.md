# Big Data Technologies Project: FISCO

The scope of this project was to design and implement a big data system that can provide credit scoring for companies that are not mandated to deposit a balance sheet (e.g., partnerships).

Each folder of the project corresponds to a step in the pipeline and is intended to run separately.
A script has been provided to run all the layers.

Every step has been divided in three folders:
1. Components, where the work not related to classes or data transportation is done;
2. Model, where all the classes are located;
3. Services, which aim is to handle data transportation between technologies;

This branch of the project works locally, for a containerized solution please refer to the branch _"Dockerized"_.

This project is licensed with the *GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007*, for more information please refer to the file **COPYING**.

Below lies a brief description of what each layer does, for a more detailed explanation consult the readme of each folder.

***Required technologies (whole pipeline)***:
+ Python (the whole project was designed tested with Python 3.10 in mind);
+ Redis;
+ Zookeeper;
+ Apache Kafka;
+ Google Cloud Storage;
+ An SQL server;
+ A hosted frontend. Due to time constraints, we decided to use Anvil, so the frontend layer will be almost empty;


## 0. Source Layer

The aim of the source layer is to generate and categorize data.
All documents are generated in the folder "components/reports".
They are later parsed into json format and sent into a temporary storage (Redis).

***An instance of Redis Server must run for this layer to work.***

## 1. Ingestion Layer

The aim of the ingestion layer is to fetch the parsed data, categorize and divide it.
A Kafka message producer will extract the data from Redis and divide it into topics before sending it.

***An instance of Zookeeper and Apache Kafka must run for this layer to work.***

## 2. Data Collector Layer

This layer will read the messages with a Kafka Listener and based on the topic it will upload them into an object storage bucket.

***An instance of Zookeeper and Apache Kafka must run for this layer to work.***

***Since Google Cloud Storage has been chosen as an object storage, the credentials json must be downloaded into the "credentials" folder.***

## 3. Data processing Layer

This layer will fetch the records from the object storage, cleaning and preparing them for the database insertion.

***An instance of Redis Server must run for this layer to work.***

## 4. Data Storage Layer 

This layer will fetch the prepared data from redis and insert it into an SQL database.

***An instance of Redis Server must run for this layer to work.***

***An instance of a mysql database also must run for this layer to work. 
We used a remote database server, so the code is expecting a file called "db-credentials.json" in the credentials' folder in order to work.***

## 5. Query Layer

This layer will act as a broker between the front-end and the back-end of the application.

***An instance of a mysql database also must run for this layer to work. 
We used a remote database server, so the code is expecting a file called "db-credentials.json" in the "credentials" folder in order to work.***

## 6. Frontend

As specified above, since the application is hosted in Anvil, the folder is currently devoided of working code.