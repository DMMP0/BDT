'''this script here is to send the personal data to the personal information table'''
from asyncio.windows_events import NULL
from matplotlib.font_manager import json_dump
import mysql.connector
from mysql.connector import Error
import json


def connect_db():
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
    return (cursor,connection)
        
        

def close_db_connection(connection,cursor):
    if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")




def send_broker_data(key):
    (cursor,connection) = connect_db()
    query = 'SELECT * FROM credit_history where fiscal_code_fk = %s'
    val = (key,)
    cursor = connection.cursor()
    cursor.execute(query,val)
    broker_data = cursor.fetchall()
    close_db_connection(connection,cursor)
    return broker_data


