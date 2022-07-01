# Query Layer

The aim of this layer is to fetch the data from the hosted database .

***NB: this layer was designed with Python 3.10 in mind.***

***NB: an sql server must be available***. A script to recreate from scratch an example of database can be found here, named "crete_database.sql".

**In order for the script to work, a json credential file must be present into the "credentials" folder.**
The credential path can be changed at the start of each service file:

*config_db = json.load(open(source + "/credentials/db-config.json"))*

***NB: No pre-req technology is requred to run this layer, all we need is the hosted database connection.*** In order to do that [Redis]Credit formulation script will get all the data from the services, set each retured table attribites as a class objects in the models, and then in components relavent files are ready to use the data for the formulation 

## Getting data from the database

The layer can be easily started by running the script 'main.py' but in frontend layer.

It will get data from database and then send it to web page.
