'''this script here is to send the firm data to the firm information table'''
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
"first_name": "carrizales", "last_name": "idiaquez", "sex": "Male", "DOB": "10/24/1961", 
"ethnicity": "native american", "education": "middle school", "phone_number": "307-166-6420",
"email": "hr@jameshardieindustriesnv.org", "purpose": "other investment", 
"registeration_number": "e48f4632-6ded-42b9-911f-63c024f30ee2", "company_name": "James Hardie Industries N.V.", 
"establied_date": "10/12/1966", "country": "Netherlands", "number_of_employes": 18}



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


    
## main
(cursor,connection) = connect_db()
send_firm_data(data,cursor,connection)
close_db_connection(cursor)