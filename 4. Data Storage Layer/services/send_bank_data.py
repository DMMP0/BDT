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


data ={"Id_Number": "a93b7ad0-deab-4e2e-9897-36741b1c7321",
"first_name": "mertie", "last_name": "ureta", "sex": "Female",
"DOB": "1/12/1970", "ethnicity": "black", "education": "no diploma",
"phone_number": "755-555-2797", "email": "mertie_ureta@gmail.com", 
"bank_name": "Swedbank", "bank_country": "Norway", "open_new_credit_in_6_months": "1",
"amount_in_6_months": "$43,956,365,609.00", "new_credit_in_12_months": "0.0", "new_credit_in_18_months": "1.0",
"amount_in_12_months": "$10,564.00", "amount_in_18_months": "$46,333,874,939.00", "house_mortgage": "True",
"amount_of_house_mortgage": "$269,659.00", "amount_due_mortgage": "$351,078.00", "house_property": "False",
"total_house_amount": "0.0", "credit_card_number": "5", "credit_card_limit_total": "162333", "actual_debit_credit_cards": "1.0",
"monthly_income": "$5,640.00", "savings": "$12,790.00", "other_savings": "$13,175.00"}



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




def send_new_credit(dict_data:dict,cursor,connection):
    tag = True
    bank_dict = Bank(dict_data)
    # print(dict.number_of_employes)
    query = 'SELECT MAX(new_credit_id) FROM new_credit'
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    if(tag):
        if(data[0] == None):
            print('here')
            mix_credit_id = 0
        else:
            mix_credit_id = data[0]+1
        insert_query = "INSERT INTO new_credit(new_credit_id,amount_in_12_months,amount_in_6_months,amount_in_18_months,last_update_time_stamp,fiscal_code_fk)"
        value_attr = "VALUES(%s,%s,%s,%s,%s,%s)"
        values = (mix_credit_id,bank_dict.amount_in_12_months,bank_dict.amount_in_6_months,bank_dict.amount_in_18_months,datetime.datetime.now(),bank_dict.fiscal_code)
        print(values)
        cursor.execute(insert_query+value_attr , values)
        print(cursor.rowcount, "was inserted.")
        connection.commit()



def send_new_credit(dict_data:dict,cursor,connection):
    tag = True
    bank_dict = Bank(dict_data)
    # print(dict.number_of_employes)
    query = 'SELECT MAX(new_credit_id) FROM new_credit'
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    if(tag):
        if(data[0] == None):
            print('here')
            mix_credit_id = 0
        else:
            mix_credit_id = data[0]+1
        insert_query = "INSERT INTO new_credit(new_credit_id,amount_in_12_months,amount_in_6_months,amount_in_18_months,last_update_time_stamp,fiscal_code_fk)"
        value_attr = "VALUES(%s,%s,%s,%s,%s,%s)"
        values = (mix_credit_id,bank_dict.amount_in_12_months,bank_dict.amount_in_6_months,bank_dict.amount_in_18_months,datetime.datetime.now(),bank_dict.fiscal_code)
        print(values)
        cursor.execute(insert_query+value_attr , values)
        print(cursor.rowcount, "was inserted.")
        connection.commit()
    
## main
(cursor,connection) = connect_db()
send_new_credit(data,cursor,connection)
close_db_connection(cursor)