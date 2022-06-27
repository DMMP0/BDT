'''this script here is to send the personal data to the personal information table'''
from asyncio.windows_events import NULL
from matplotlib.font_manager import json_dump
import mysql.connector
from mysql.connector import Error
import sys,os
import json
import datetime

# curr = os.path.dirname(os.path.curdir)

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




def send_person_data(dict_data:dict,cursor,connection):
    tag = True
    person_dict = Person(dict_data)
    # print(dict.number_of_employes)
    query = 'SELECT MAX(person_id),fiscal_code FROM personal_data'
    cursor = connection.cursor()
    cursor.execute(query)
    firm_data = cursor.fetchall()
    print(firm_data)
    for row in firm_data :
        print(row)
        if(row[1] == person_dict.fiscal_code):
            tag = False
    if(tag):
        if(row[0] == None):
            print('here')
            person_id = 0
        else:
            person_id = row[0]+1

        insert_query = "INSERT INTO personal_data(person_id,fiscal_code,first_name,last_name,sex,date_of_birth,ethnicity,highest_degree,address,email,phone_number,state,firm_registration,last_update_time_stamp)"
        value_attr = "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (person_id,person_dict.fiscal_code,person_dict.first_name,person_dict.last_name,person_dict.sex,person_dict.DOB,person_dict.ethnicity,person_dict.education,person_dict.state,person_dict.email,person_dict.phone_number,person_dict.country,person_dict.firm_registeration_number,datetime.datetime.now())
        print(values)
        cursor.execute(insert_query+value_attr , values)
        print(cursor.rowcount, "was inserted.")
        connection.commit()
    
    
## main
(cursor,connection) = connect_db()
send_person_data(data,cursor,connection)
close_db_connection(cursor)