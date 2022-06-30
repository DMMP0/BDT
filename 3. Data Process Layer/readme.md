# Process Layer

The aim of this layer is to fetch the categorized data from the object storage, process it and send the processed data to a persistence layer.

***NB: this layer was designed with Python 3.10 in mind.***

***NB: this layer has been designed to work with Google Cloud Storage as an object storage***.

**In order for the script to work, a json credential file must be present into the "credentials" folder.**
The credential path can be changed in the file models/temp_storage_retriever at line 11.

The buckets to read from were created with the following logic: kafka_topic-bdt-13 *(e.g. bank-bdt-13)*.  The name can be changed in the main.py, line 12 -> 15.

***NB: an instance of redis-server must run in order for this layer to work.*** In order to do that [Redis](https://redis.io/download/) must be downloaded.
Once downloaded and installed, an instance of Redis server can simply be started by typing *redis-server* in your terminal.
If you want to check what's going under the hood, you can get all the keys with the command _'keys \*_'. If you already have other keys in your redis instance, a better
option would be _'keys \*(\*-report-row)\*'_. If you want to see the content of a specific key, the command _'get "**Key name**"'_ shold be issued. For multiple keys, the command _mget_
can be used. 

## Start processing

The layer can be easily started by running the script 'main.py'.

The script will fetch data from cloud storage, process it and divide it in order for each record to become 1 or multiple records of the database structure.

The processing was designed with flexibility in mind, so the processing functions and synonym dictionaries can be found in models/utils.py

Processed records will be sent to redis in json format with the following key logic: (table-report-row)randomcharacters (e.g. "(broker-report-row)MIuInyBCZkhIutwSLxmr")
