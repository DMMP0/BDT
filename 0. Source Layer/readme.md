# Source Layer

The aim of this layer is to generate and parse the data, sending it to Redis (the persistence layer).

***NB: this layer was designed with Python 3.10 in mind.***

***NB: an instance of redis-server must run in order for this layer to work.*** In order to do that [Redis](https://redis.io/download/) must be downloaded.
Once downloaded and installed, an instance of Redis server can simply be started by typing *redis-server* in your terminal.
If you want to check what's going under the hood, you can get all the keys with the command _'keys \*_'. If you already have other keys in your redis instance, a better
option would be _'keys \*(\*).\*'_. If you want to see the content of a specific key, the command _'get "**Key name**"'_ shold be issued. For multiple keys, the command _mget_
can be used. 

## Data generation 

In order to start the data 