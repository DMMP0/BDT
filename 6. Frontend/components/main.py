import anvil.server
import json
import anvil.server
import mysql.connector
from mysql.connector import Error

anvil.server.connect('NKBJP7OHDHIAKL4IW2C2FOWE-UZZP33BE5EVXZYOW')


with open("..\..\credentials\db-config.json", "r") as jsonfile:
    config_db = json.load(jsonfile) # Reading the file
    jsonfile.close()
try:

    connection = mysql.connector.connect(host=config_db['host'],
                                            database=config_db['database'],
                                            user=config_db['user'],
                                            password=config_db['password'])
    if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            print("You're connected to database: ")

except Error as e:
    print("Error while connecting to MySQL", e)


@anvil.server.callable
def get_items(id):
    query = 'SELECT * FROM personal_data WHERE fiscal_code = %s'
    val =(str(id),)
    cursor.execute(query,val)
    items = cursor.fetchall()
    return [
        {'id': item[1], 'fname': item[2], 'lname': item[3]}
        for item in items
    ]
print('here')

anvil.server.wait_forever()