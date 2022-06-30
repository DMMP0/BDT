'''this script here is to send the personal data to the personal information table'''


import redis

import mysql.connector
from mysql.connector import Error
import os
import json
import datetime


source = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the parent directory
from .get_data_from_redis import get_dicts_from_redis

config_db = json.loads(os.environ['CREDENTIALS'])



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

def find_fk(dict_data:dict,cursor,connection)->bool:
    tag = True
    # print(dict.number_of_employes)
    query = 'SELECT fiscal_code FROM personal_data'
    cursor = connection.cursor()
    cursor.execute(query)
    personal_data = cursor.fetchall()
    for row in personal_data :
        # print(row)
        if(row[0] == dict_data['fiscal_code']):
            tag = False
    return tag


def send_questura_data(dict_data:dict,cursor,connection):
    tag = True
    # print(dict.number_of_employes)
    query = 'SELECT MAX(criminal_id) FROM criminal_records'
    cursor = connection.cursor()
    cursor.execute(query)
    firm_data = cursor.fetchall()
    for row in firm_data :
        criminal_id = row[0]
    if(tag):
        if(criminal_id== None):
            # print('here')
            criminal_id = 0
        else:
            criminal_id = criminal_id+1

    if(find_fk(dict_data,cursor,connection) == False): #  %s,       %s,        %s,          %s,       %s,      %s,       %s,                   %s
        insert_query = "INSERT INTO criminal_records(criminal_id,bankrupty,investigation,accused,condemned,civ_pass,last_updated_time_stamp,fiscal_code_fk)"
        value_attr = "VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (criminal_id,dict_data['bankruptcy'],dict_data['investigation'],dict_data['accused'],
                  dict_data['condamned'],dict_data['civ_pass'],datetime.datetime.now(),dict_data['fiscal_code'])
        # print(values)
        try:
            cursor.execute(insert_query + value_attr, values)
            print(cursor.rowcount, "was inserted (questura).")
        except mysql.connector.errors.IntegrityError:
            print("Duplicated key not inserted")
        connection.commit()
    else:
        print("personal data not found")


    
## main
def main(r: redis.StrictRedis):
    questura_dicts, keys_to_delete = get_dicts_from_redis('criminal_records')
    if questura_dicts == False:
        print("No new questura data")
        return
    (cursor,connection) = connect_db()
    for questura_dict in questura_dicts:
        send_questura_data(questura_dict,cursor,connection)
    close_db_connection(connection,cursor)
    if keys_to_delete:
        r.delete(*keys_to_delete)
