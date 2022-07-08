# Process Layer

The aim of this layer is to fetch the categorized data from the object storage, process it and send the processed data to a persistence layer.

***NB: this layer was designed with Python 3.10 in mind.***

***NB: this layer has been designed to work with Google Cloud Storage as an object storage***.

**In order for the script to work, a json credential file must be passed as an environment variable**

The buckets to read from were created with the following logic: kafka_topic-bdt-13 *(e.g. bank-bdt-13)*.  The name can be changed in the main.py, line 12 -> 15.

***NB: an instance of a redis container must run in order for this layer to work.*** 
It can be instantiated with the following command: *docker run -d --name redis --network app-tier redis*

## Start processing

The program can be started by:
1. creating the environment variable: *credentials=$(< ../credentials/bdt-project-200-6164fe338b7d.json)*
2. building the image: *docker build -t bdt/process-layer .*
3. starting the container: *docker run -e "CREDENTIALS=$credentials" -d --name 3-Process-Layer-BDT  --network app-tier bdt/process-layer*