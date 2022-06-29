'''this script here is to send the personal data to the personal information table'''

import mysql.connector
from mysql.connector import Error
import sys,os
import json
import datetime


source = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the parent directory


config_db = json.load(open(source + "/credentials/db-config.json"))
from .get_data_from_redis import get_dicts_from_redis

import  redis





def connect_db():

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




def send_broker_data(dict_data:dict,cursor,connection):
    tag = True
    # print(dict.number_of_employes)
    query = 'SELECT MAX(credit_history_id) FROM credit_history'
    cursor = connection.cursor()
    cursor.execute(query)
    broker_data = cursor.fetchall()
    for row in broker_data :
       broker_id = row[0]
    if(tag):
        if(row[0] == None):
            print('here')
            broker_id = 0
        else:
            broker_id = row[0]+1
        insert_query = "INSERT INTO credit_history(credit_history_id,from30to60,from60to90,more_than_90,insolvent_ammount,last_update_time_stamp,fiscal_code_fk)"
        value_attr = "VALUES(%s,%s,%s,%s,%s,%s,%s)"
        values = (broker_id,dict_data['from30to60'],dict_data['from60to90'],dict_data['morethan90'],
                  dict_data['insolvent_amount'],datetime.datetime.now(),dict_data['fiscal_code'])
        print("broker data")
        try:
            cursor.execute(insert_query+value_attr , values)
            print(cursor.rowcount, "was inserted.")
        except mysql.connector.errors.IntegrityError:
            print("Duplicated key not inserted")
        connection.commit()


    
## main
def main(r: redis.StrictRedis):
    broker_dicts, keys_to_delete = get_dicts_from_redis('broker')
    if broker_dicts == False:
        print("No new broker data")
        return
    (cursor,connection) = connect_db()
    for broker_dict in broker_dicts:
        send_broker_data(broker_dict,cursor,connection)
    close_db_connection(connection,cursor)
    if keys_to_delete:
        r.delete(*keys_to_delete)