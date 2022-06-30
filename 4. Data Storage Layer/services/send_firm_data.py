'''this script here is to send the firm data to the firm information table'''

import mysql.connector
from mysql.connector import Error
import sys, os

import datetime
import json

source = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the parent directory
from .get_data_from_redis import get_dicts_from_redis

config_db = json.load(open(source + "/credentials/db-config.json"))
import redis

'''
['CNIC',ID,Fiscal,Fiscal code,id_number,identity number]
for the first key find if the list have same name . if yes - > Id_Number
'''


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
    return (cursor, connection)


def close_db_connection(connection, cursor):
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


def send_firm_data(dict_data: dict, cursor, connection):
    tag = True
    # print(dict.number_of_employes)
    query = 'SELECT MAX(firm_data_id),registeration_number FROM firm_data'
    cursor = connection.cursor()
    cursor.execute(query)
    firm_data = cursor.fetchall()
    for row in firm_data:
        print(row)
        if (row[1] == dict_data['registeration_number']):
            tag = False
    if (tag):
        if (row[0] == None):
            print('here')
            firm_id = 0
        else:
            firm_id = row[0] + 1
        insert_query = "INSERT INTO firm_data(firm_data_id,registeration_number,firm_name,established_date,number_of_employes,country,last_update_time_stamp) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        # value_attr = "VALUES(%s,%s,%s,%s,%s,%s,%s)"
        values = (firm_id, dict_data['registeration_number'], dict_data['company_name'], dict_data['established_date'],
                  dict_data['number_of_employes'], dict_data['country'], datetime.datetime.now()) #,dict_data['email'])
        print("(firm data)")
        try:
            cursor.execute(insert_query, values)
            # print(cursor.rowcount, "was inserted.")
        except mysql.connector.errors.IntegrityError:
            print(cursor.rowcount, ": Key already inserted, skipping")

        connection.commit()


def send_credit_data(dict_data: dict, cursor, connection):
    tag = True
    # print(dict.number_of_employes)
    query = 'SELECT MAX(credit_data_id) FROM credit_data'
    cursor = connection.cursor()
    cursor.execute(query)
    firm_data = cursor.fetchall()
    for row in firm_data:
        firm_data = row[0]
    if (tag):
        if (row[0] == None):
            print('here')
            firm_id = 0
        else:
            firm_id = row[0] + 1
        insert_query = "INSERT INTO credit_data(credit_data_id,firm_registeration_number,amount_of_credit,purpose,duration_in_months,last_update_time_stamp)"
        value_attr = "VALUES(%s,%s,%s,%s,%s,%s)"
        values = (
            firm_id, dict_data['registeration_number'], dict_data['amount_of_credit'], dict_data['purpose'],
            dict_data['duration_in_months'], datetime.datetime.now())
        # print(values)
        try:
            cursor.execute(insert_query + value_attr, values)
            print(cursor.rowcount, "was inserted.(credit data)")
        except mysql.connector.errors.IntegrityError:
            print("Duplicated key not inserted")
        print(cursor.rowcount, "was inserted.")
        connection.commit()


## main
def main(r: redis.StrictRedis):
    keys_to_delete = list()
    t = get_dicts_from_redis('firm')
    if t[0] != False:
        firm_dicts = t[0]
        keys_to_delete += t[1]
    else:
        firm_dicts = []
        print("No new firm data")


    t = get_dicts_from_redis('credit_data')
    if t[0] != False:
        credit_data_dicts = t[0]
        keys_to_delete += t[1]
    else:
        credit_data_dicts = []
        print("No new credit_data data")


    (cursor, connection) = connect_db()
    for firm_dict in firm_dicts:
        send_firm_data(firm_dict, cursor, connection)
    for credit_data_dict in credit_data_dicts:
        send_credit_data(credit_data_dict, cursor, connection)
    close_db_connection(connection, cursor)
    if keys_to_delete:
        r.delete(*keys_to_delete)
