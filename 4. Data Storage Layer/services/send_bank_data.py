'''this script here is to send the bank data to the 4 tables in the database, 
1. Credit mix table
2. asset
3. losses
new credit'''
from asyncio.windows_events import NULL
from matplotlib.font_manager import json_dump
import mysql.connector
from mysql.connector import Error
import sys,os
import json
import datetime
from send_personal_data import send_person_data


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the parent directory
from models.bank import Bank
from models.broker import Broker
from models.questura import Questura
from models.statement import Statement
from models.person_info import Person


data ={"Id_Number": "13a9cd05-07ba-4d47-8a46-1cfa22b045a6",
"first_name": "mertie", "last_name": "ureta", "sex": "Female",
"DOB": "1/12/1970", "ethnicity": "black", "education": "no diploma",
"phone_number": "755-555-2797", "email": "mertie_ureta@gmail.com", 
"bank_name": "Swedbank", "bank_country": "Norway", "open_new_credit_in_6_months": 1,
"amount_in_6_months": 43956365609.00, "new_credit_in_12_months": 0, "new_credit_in_18_months": 1,
"amount_in_12_months": 10564.00, "amount_in_18_months": 46333874939.00, "house_mortgage": True,
"amount_of_house_mortgage": 269659.00, "amount_due_mortgage": 351078.00, "house_property": "False",
"total_house_amount": 0, "credit_card_number": 5, "credit_card_limit_total": 162333, "actual_debit_credit_cards": 1,
"monthly_income": 5640.00, "savings": 12790.00, "other_savings": 13175.00}



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


def find_fk(dict_data:dict,cursor,connection)->bool:
    tag = True
    person_dict = Questura(dict_data)
    query = 'SELECT fiscal_code FROM personal_data'
    cursor = connection.cursor()
    cursor.execute(query)
    personal_data = cursor.fetchall()
    for row in personal_data :
        if(row[0] == person_dict.fiscal_code):
            tag = False
    return tag

def send_new_credit(dict_data:dict,cursor,connection):
    # send_person_data(dict_data,cursor,connection)
    tag = True
    bank_dict = Bank(dict_data)
    mix_credit_id = 0
    query = 'SELECT MAX(new_credit_id) FROM new_credit'
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data :
        mix_credit_id = row[0]
    if(tag):
        if(mix_credit_id == None):
            mix_credit_id = 0
        else:
            mix_credit_id += 1
    if(find_fk(dict_data,cursor,connection) == False):
        insert_query = "INSERT INTO new_credit(new_credit_id,amount_in_12_months,amount_in_6_months,amount_in_18_months,last_update_time_stamp,fiscal_code_fk)"
        value_attr = "VALUES(%s,%s,%s,%s,%s,%s)"
        values = (mix_credit_id,bank_dict.amount_in_12_months,bank_dict.amount_in_6_months,bank_dict.amount_in_18_months,datetime.datetime.now(),bank_dict.fiscal_code)
        cursor.execute(insert_query+value_attr , values)
        print(cursor.rowcount, "was inserted.")
        connection.commit()



def send_credit_mix(dict_data:dict,cursor,connection):
    # send_person_data(dict_data,cursor,connection)
    tag = True
    bank_dict = Bank(dict_data)
    mix_credit_id = 0
    query = 'SELECT MAX(credit_mix_id) FROM credit_mix'
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data :
        mix_credit_id = row[0]
    if(tag):
        if(mix_credit_id == None):
            mix_credit_id = 0
        else:
            mix_credit_id += 1
    if(find_fk(dict_data,cursor,connection) == False):
        insert_query = "INSERT INTO credit_mix(credit_mix_id,installment,house_mortgage,credit_card_number,last_update_time_stamp,fiscal_code_fk)"
        value_attr = "VALUES(%s,%s,%s,%s,%s,%s)"
        values = (mix_credit_id,'yes',bank_dict.house_mortgage,bank_dict.credit_card_number,datetime.datetime.now(),bank_dict.fiscal_code)

        cursor.execute(insert_query+value_attr , values)
        print(cursor.rowcount, "was inserted.")
        connection.commit()

def send_assets_data(dict_data:dict,cursor,connection):
    # send_person_data(dict_data,cursor,connection)
    tag = True
    bank_dict = Bank(dict_data)
    query = 'SELECT MAX(asset_id) FROM assets'
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data :
        asset_id = row[0]
    if(tag):
        if(asset_id == None):
            asset_id = 0
        else:
            asset_id += 1
    if(find_fk(dict_data,cursor,connection) == False):
        insert_query = "INSERT INTO assets(asset_id,total_amount_of_house,monthly_income,savings,other_savings,last_updated_time_stamp,fiscal_code_fk)"
        value_attr = "VALUES(%s,%s,%s,%s,%s,%s,%s)"
        values = (asset_id,bank_dict.total_house_amount,bank_dict.monthly_income,bank_dict.savings,bank_dict.other_savings,datetime.datetime.now(),bank_dict.fiscal_code)
        cursor.execute(insert_query+value_attr , values)
        print(cursor.rowcount, "was inserted.")
        connection.commit()


def send_losses_data(dict_data:dict,cursor,connection):
    # send_person_data(dict_data,cursor,connection)
    tag = True
    bank_dict = Bank(dict_data)
    query = 'SELECT MAX(losses_id) FROM losses'
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data :
        losses_id = row[0]
    if(tag):
        if(losses_id == None):
            losses_id = 0
        else:
            losses_id += 1
    if(find_fk(dict_data,cursor,connection) == False):
        insert_query = "INSERT INTO losses(losses_id,actual_debit_credit_cards,amount_due_mortgage,last_update_time_stamp,fiscal_code_fk)"
        value_attr = "VALUES(%s,%s,%s,%s,%s)"
        values = (losses_id,bank_dict.actual_debit_credit_cards,bank_dict.amount_due_mortgage,datetime.datetime.now(),bank_dict.fiscal_code)
        cursor.execute(insert_query+value_attr , values)
        print(cursor.rowcount, "was inserted.")
        connection.commit()
    
## main
(cursor,connection) = connect_db()
# send_new_credit(data,cursor,connection)
# send_credit_mix(data,cursor,connection)
# send_assets_data(data,cursor,connection)
# send_losses_data(data,cursor,connection)
close_db_connection(cursor)