# Big Data Technologies Project: FISCO

The scope of this project was to design and implement a big data system that can provide credit scoring for companies that are not mandated to deposit a balance sheet (e.g., partnerships).

Each folder of the project corresponds to a step in the pipeline and is intended to run separately.

Every step has been divided in three folders:
1. components, where the work not related to classes or data transportation is done
2. model, where all the classes are located
3. services, which aim is to handle data transportation between technologies

This branch of the project works locally, for a containerized solution please refer to the branch _"Dockerized"_
This project is licensed with the *GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007*, for more information please refer to the file **COPYING**.

Below lies a brief description of what each layer does, for a more detailed explanation consult the readme of each folder.
***Required technologies (whole pipeline)***:
+ Python (the whole project was designed tested with Python 3.10 in mind)
+ Redis
+ Apache Kafka
+ Google Cloud Storage
+ An SQL server
+ A hosted frontend. Due to time constraints, we decided to 



## 0. Source Layer

The aim of the source layer is to generate and categorize data.
All documents are generated in the folder "components/reports".
They are later parsed into json format and sent as Kafka messages