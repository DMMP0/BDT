# Collector Layer

The aim of this layer is to fetch the categorized data from kafka and upload it to an object storage.

***NB: this layer was designed with Python 3.10 in mind.***

***NB: this layer requires an instance of Zookeeper and Apache Kafka Running***.
They can be both installed and initialized with the following commands:

*docker run -d --name zookeeper-server --network app-tier -e ALLOW_ANONYMOUS_LOGIN=yes bitnami/zookeeper:latest*

*docker run -d --name kafka-server --network app-tier -e ALLOW_PLAINTEXT_LISTENER=yes -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper-server:2181 bitnami/kafka:latest*

***NB: this layer has been designed to work with Google Cloud Storage as an object storage***.

**In order for the script to work, a json credential file must be passed as an environment variable**

**The script does not create the buckets automatically**, they were created with the following logic: kafka_topic-bdt-13 *(e.g. bank-bdt-13)*.  The name can be changed at models/message_consumer.py, line 21.

If you wish to **delete all files sent into a bucket**, the following command must be issued in the Google Cloud shell: gsutil -m rm -r gs://bucket-name/\*


## Start the collection

The program can be started by:
1. creating the environment variable: *credentials=$(< ../credentials/bdt-project-200-6164fe338b7d.json)*
2. building the image: *docker build -t bdt/collector-layer .*
3. starting the container: *docker run -e "CREDENTIALS=$credentials" -d --name 2-Collector-Layer-BDT  --network app-tier bdt/collector-layer*
