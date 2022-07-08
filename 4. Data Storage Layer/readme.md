# Storage Layer

The aim of this layer is to fetch the processed data from the previous persistence layer and send it to the database.

***NB: this layer was designed with Python 3.10 in mind.***

***NB: an sql container be available***. 
A script to recreate from scratch an example of database can be found here in the general directory".

**In order for the script to work, a json credential file must be present into the "credentials" folder.**
The credential path can be changed at the start of each service file:

*config_db = json.load(open(source + "/credentials/db-config.json"))*

***NB: an instance of redis-server must run in order for this layer to work.*** In order to do that [Redis](https://redis.io/download/) must be downloaded.
Once downloaded and installed, an instance of Redis server can simply be started by typing *redis-server* in your terminal.
If you want to check what's going under the hood, you can get all the keys with the command _'keys \*_'. If you already have other keys in your redis instance, a better
option would be _'keys \*(\*-report-row)\*'_. If you want to see the content of a specific key, the command _'get "**Key name**"'_ shold be issued. For multiple keys, the command _mget_
can be used.

## Sending data to storage

The layer can be easily started by running the script 'main.py'.

It will get data from redis and then send it to a remote database.

Since there is a specific data sending order to endure constraints in the database,
the script will start by sending the firm data of the current batch, then it will send the personal data and finally it 
will send the other categories in a multithreaded way