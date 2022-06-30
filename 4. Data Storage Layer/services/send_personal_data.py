'''this script here is to send the personal data to the personal information table'''

import mysql.connector
from mysql.connector import Error
import sys,os
import json
import datetime

# curr = os.path.dirname(os.path.curdir)


import redis
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




def send_person_data(dict_data:dict,cursor,connection):
    tag = True
    # print(dict.number_of_employes)
    query = 'SELECT MAX(person_id),fiscal_code FROM personal_data'
    cursor = connection.cursor()
    cursor.execute(query)
    firm_data = cursor.fetchall()
    print(firm_data)
    for row in firm_data :
        print(row)
        if(row[1] == dict_data['fiscal_code']):
            tag = False
    if(tag):
        if(row[0] == None):
            print('here')
            person_id = 0
        else:
            person_id = row[0]+1

        insert_query = "INSERT INTO personal_data(person_id,fiscal_code,first_name,last_name,sex,date_of_birth,ethnicity,highest_degree,address,email,phone_number,state,firm_registration,last_update_time_stamp)"
        value_attr = "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (person_id,dict_data['fiscal_code'],dict_data['first_name'], dict_data['last_name'], dict_data['sex'],
                  dict_data['DOB'],dict_data['ethnicity'], dict_data['highest_degree'],dict_data['address'],
                  dict_data['email'], dict_data['phone_number'],dict_data['state'],
                  dict_data['firm_registration'],datetime.datetime.now())
        # print(values)
        try:
            cursor.execute(insert_query + value_attr, values)
            print(cursor.rowcount, "was inserted(personal data).")
        except mysql.connector.errors.IntegrityError:
            print("Duplicated key not inserted")
        # print(cursor.rowcount, "was inserted.")
        connection.commit()
    
    
## main
def main(r: redis.StrictRedis):
    person_dicts, keys_to_delete = get_dicts_from_redis('personal_data')
    if person_dicts == False:
        print("No new personal data")
        return
    (cursor,connection) = connect_db()
    for person_dict in person_dicts:
        send_person_data(person_dict,cursor,connection)
    close_db_connection(connection,cursor)
    if keys_to_delete:
        r.delete(*keys_to_delete)
