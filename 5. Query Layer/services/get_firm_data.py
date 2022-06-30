'''this script here is to send the personal data to the personal information table'''

from matplotlib.font_manager import json_dump
import mysql.connector
from mysql.connector import Error
import sys,os
import json
import datetime


def connect_db():
    config_db = json.loads(os.environ['CREDENTIALS'])
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




def get_firm_data(firm):
    (cursor,connection) = connect_db()
    query = 'SELECT * FROM firm_data where registeration_number = %s'
    val = (firm,)
    cursor = connection.cursor()
    cursor.execute(query,val)
    if (cursor.description is None):
        return []
    else:
        data = cursor.fetchall()
        close_db_connection(connection,cursor)
        return data

def get_credit_data(firm):
    (cursor,connection) = connect_db()
    query = 'SELECT * FROM credit_data where firm_registeration_number = %s'
    val = (firm,)
    cursor = connection.cursor()
    cursor.execute(query,val)
    if (cursor.description is None):
        return []
    else:
        data = cursor.fetchall()
        close_db_connection(connection,cursor)
        return data
