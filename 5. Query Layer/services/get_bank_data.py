'''this script here is to send the bank data to the 4 tables in the database, 
1. Credit mix table
2. asset
3. losses
new credit'''
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



def get_new_credit(key):
    # send_person_data(dict_data,cursor,connection)
    (cursor,connection) = connect_db()
    query = 'SELECT * FROM new_credit where fiscal_code_fk = %s'
    val = (key,)
    cursor = connection.cursor()
    cursor.execute(query,val)
    data = cursor.fetchall()
    close_db_connection(connection,cursor)
    return data    



def get_credit_mix(key):
    # send_person_data(dict_data,cursor,connection)
    (cursor,connection) = connect_db()
    query = 'SELECT * FROM credit_mix where fiscal_code_fk = %s'
    val = (key,)
    cursor = connection.cursor()
    cursor.execute(query,val)
    data = cursor.fetchall()
    close_db_connection(connection,cursor)
    return data
    

def get_assets_data(key:str):
    # send_person_data(dict_data,cursor,connection)
    (cursor,connection) = connect_db()
    query = "SELECT * FROM assets where fiscal_code_fk = %s "
    val = (key,)
    cursor = connection.cursor()
    cursor.execute(query,val)
    data = cursor.fetchall()
    close_db_connection(connection,cursor)
    return data  
    


def get_losses_data(key):
    (cursor,connection) = connect_db()
    query = 'SELECT * FROM losses where fiscal_code_fk = %s'
    val = (key,)
    cursor = connection.cursor()
    cursor.execute(query,val)
    data = cursor.fetchall()
    close_db_connection(connection,cursor)
    return data  
    




def get_bank_data():
    # check first if the data has been there already
    (cursor,connection) = connect_db()
    query = 'SELECT * FROM bank_data'
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    close_db_connection(connection,cursor)
    return data  

    
def get_person_banks(key):
    (cursor,connection) = connect_db()
    query = 'SELECT * FROM 	bank_person_relationships WHERE person_id = %s'
    val = (key,)
    cursor = connection.cursor()
    cursor.execute(query,val)
    data = cursor.fetchall()
    close_db_connection(connection,cursor)
    return data  
    
