'''this script here is to send the personal data to the personal information table'''
from asyncio.windows_events import NULL
from matplotlib.font_manager import json_dump
import mysql.connector
from mysql.connector import Error
import sys,os
import json
import datetime


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the parent directory
from models.bank import Bank
from models.broker import Broker
from models.questura import Questura
from models.statement import Statement
from models.person_info import Person


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




def get_person_data(key):
    (cursor,connection) = connect_db()
    tag = True
    query = 'SELECT * FROM personal_data Where fiscal_code=%s'
    val = (key,)
    cursor = connection.cursor()
    cursor.execute(query,val)
    person_data = cursor.fetchall()
    close_db_connection(connection,cursor)
    return person_data

