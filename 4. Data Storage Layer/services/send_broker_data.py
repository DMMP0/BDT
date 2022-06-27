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


data ={"Id_Number": "13a9cd05-07ba-4d47-8a46-1cfa22b045a6",
"first_name": "mertie", "last_name": "ureta", "sex": "Female", "DOB": "1/12/1970",
"ethnicity": "black", "education": "no diploma", "phone_number": "755-555-2797", 
"email": "mertie_ureta@gmail.com", "agency_country": "Czech Republic", "agency_name": "experian",
"from30to60": 3, "from60to90": 3, "morethan90": 2, "debit_id": 5223375666475302, "insolvent": False, 
"insolvent_ammount": 42261306500.00}

# TODO: to get data from redis:

# broker_dict = get_dicts_from_redis('broker')


def connect_db():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='credit_scoring',
                                            user='root',
                                            password='123$Weet')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            # cursor.execute("select database();")
            # record = cursor.fetchone()
            print("You're connected to database: ")

    except Error as e:
        print("Error while connecting to MySQL", e)

    return (cursor,connection)
        

def close_db_connection(cursor):
    if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")




def send_broker_data(dict_data:dict,cursor,connection):
    tag = True
    broker_dict = Broker(dict_data)
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
        values = (broker_id,broker_dict.from30to60,broker_dict.from60to90,broker_dict.morethan90,broker_dict.insolvent_ammount,datetime.datetime.now(),broker_dict.fiscal_code)
        print(values)
        cursor.execute(insert_query+value_attr , values)
        print(cursor.rowcount, "was inserted.")
        connection.commit()


    
## main
(cursor,connection) = connect_db()
send_broker_data(data,cursor,connection)
close_db_connection(cursor)