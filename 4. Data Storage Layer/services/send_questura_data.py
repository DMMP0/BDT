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
"first_name": "kujuan", "last_name": "ronero", 
"sex": "Female", "DOB": "6/25/1982", "ethnicity": "mix",
"education": "bachelor", "phone_number": "313-312-0697", "email": "kujuan_ronero@gmail.com",
"questura_country": "Switzerland", "bankruptcy": True, "inscred": 1016386.00, 
"fraudis": True, "investegation": True, "accused": True, "condamned": True, "civ_pass": True}



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

def find_fk(dict_data:dict,cursor,connection)->bool:
    tag = True
    person_dict = Questura(dict_data)
    # print(dict.number_of_employes)
    query = 'SELECT fiscal_code FROM personal_data'
    cursor = connection.cursor()
    cursor.execute(query)
    personal_data = cursor.fetchall()
    for row in personal_data :
        print(row)
        if(row[0] == person_dict.fiscal_code):
            tag = False
    return tag


def send_questura_data(dict_data:dict,cursor,connection):
    tag = True
    questura_dict = Questura(dict_data)
    # print(dict.number_of_employes)
    query = 'SELECT MAX(criminal_id) FROM criminal_records'
    cursor = connection.cursor()
    cursor.execute(query)
    firm_data = cursor.fetchall()
    for row in firm_data :
        criminal_id = row[0]
    if(tag):
        if(criminal_id== None):
            print('here')
            criminal_id = 0
        else:
            criminal_id = criminal_id+1

    if(find_fk(dict_data,cursor,connection) == False):
        insert_query = "INSERT INTO criminal_records(criminal_id,bankrupty,fraudis,investigation,accused,condemned,civ_pass,last_updated_time_stamp,fiscal_code_fk)"
        value_attr = "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (criminal_id,questura_dict.bankruptcy,questura_dict.fraudis,questura_dict.investigation,questura_dict.accused,questura_dict.condamned,questura_dict.civ_pass,datetime.datetime.now(),questura_dict.fiscal_code)
        print(values)
        cursor.execute(insert_query+value_attr , values)
        print(cursor.rowcount, "was inserted.")
        connection.commit()
    else:
        print("personal data not found")


    
## main
(cursor,connection) = connect_db()
send_questura_data(data,cursor,connection)
close_db_connection(cursor)