'''this script here is to send the firm data to the firm information table'''
from asyncio.windows_events import NULL
from matplotlib.font_manager import json_dump
import mysql.connector
from mysql.connector import Error
import sys,os
import json
import datetime
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the parent directory
from models.bank import Bank
from models.broker import Broker
from models.questura import Questura
from models.statement import Statement
from models.person_info import Person
# config_db = json.load("..\credentials\db-config.json")


data ={"Id_Number": "13a9cd05-07ba-4d47-8a46-1cfa22b045a6",
"first_name": "carrizales", "last_name": "idiaquez", "sex": "Male", "DOB": "10/24/1961", 
"ethnicity": "native american", "education": "middle school", "phone_number": "307-166-6420",
"email": "hr@jameshardieindustriesnv.org", "purpose": "other investment", 
"registeration_number": "e48f4632-6ded-42b9-911f-63c024f30ee2", "company_name": "James Hardie Industries N.V.", 
"establied_date": "10/12/1966", "country": "Netherlands", "number_of_employes": 18,
"amount_of_credit":2000000,"purpose":"Employee","duration_in_months":18}

# TODO: to get data from redis:

# firm_dict = get_dicts_from_redis('firm')
# credit_data ?


'''
['CNIC',ID,Fiscal,Fiscal code,id_number,identity number]
for the first key find if the list have same name . if yes - > Id_Number
'''



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
        

def close_db_connection(cursor):
    if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")




def send_firm_data(dict_data:dict,cursor,connection):
    tag = True
    firm_dict = Statement(dict_data)
    # print(dict.number_of_employes)
    query = 'SELECT MAX(firm_data_id),registeration_number FROM firm_data'
    cursor = connection.cursor()
    cursor.execute(query)
    firm_data = cursor.fetchall()
    for row in firm_data :
        print(row)
        if(row[1] == firm_dict.registeration_number):
            tag = False
    if(tag):
        if(row[0] == None):
            print('here')
            firm_id = 0
        else:
            firm_id = row[0]+1
        insert_query = "INSERT INTO firm_data(firm_data_id,registeration_number,firm_name,established_date,number_of_employes,country,last_update_time_stamp) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        # value_attr = "VALUES(%s,%s,%s,%s,%s,%s,%s)"
        values = (firm_id,firm_dict.registeration_number,firm_dict.company_name,firm_dict.established_date,firm_dict.number_of_employes,firm_dict.country,datetime.datetime.now())
        print(values)
        cursor.execute(insert_query , values)
        print(cursor.rowcount, "was inserted.")
        connection.commit()


def send_credit_data(dict_data:dict,cursor,connection):
    tag = True
    firm_dict = Statement(dict_data)
    # print(dict.number_of_employes)
    query = 'SELECT MAX(credit_data_id) FROM credit_data'
    cursor = connection.cursor()
    cursor.execute(query)
    firm_data = cursor.fetchall()
    for row in firm_data :
        firm_data = row[0]
    if(tag):
        if(row[0] == None):
            print('here')
            firm_id = 0
        else:
            firm_id = row[0]+1
        insert_query = "INSERT INTO credit_data(credit_data_id,firm_registeration_number,amount_of_credit,purpose,duration_in_months,last_update_time_stamp)"
        value_attr = "VALUES(%s,%s,%s,%s,%s,%s)"
        values = (firm_id,firm_dict.registeration_number,firm_dict.amount_of_credit,firm_dict.purpose,firm_dict.duration_in_months,datetime.datetime.now())
        print(values)
        cursor.execute(insert_query+value_attr , values)
        print(cursor.rowcount, "was inserted.")
        connection.commit()


    
## main
(cursor,connection) = connect_db()
# send_firm_data(data,cursor,connection)
# send_credit_data(data,cursor,connection)
# close_db_connection(cursor)