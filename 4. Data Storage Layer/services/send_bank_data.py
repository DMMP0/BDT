'''this script here is to send the bank data to the 4 tables in the database, 
1. Credit mix table
2. asset
3. losses
new credit'''

import mysql.connector
from mysql.connector import Error
import os
import json
import datetime
import redis
source = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the parent directory


config_db = json.load(open(source + "/credentials/db-config.json"))

from .get_data_from_redis import get_dicts_from_redis



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


def find_fk(dict_data: dict, cursor, connection) -> bool:
    tag = True

    query = 'SELECT fiscal_code FROM personal_data'
    cursor = connection.cursor()
    cursor.execute(query)
    personal_data = cursor.fetchall()
    for row in personal_data:
        if row[0] == dict_data['fiscal_code']:
            tag = False
    return tag


def send_new_credit(dict_data: dict, cursor, connection):
    # send_person_data(dict_data,cursor,connection)
    tag = True

    mix_credit_id = 0
    query = 'SELECT MAX(new_credit_id) FROM new_credit'
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        mix_credit_id = row[0]
    if (tag):
        if (mix_credit_id == None):
            mix_credit_id = 0
        else:
            mix_credit_id += 1
    if (find_fk(dict_data, cursor, connection) == False):
        insert_query = "INSERT INTO new_credit(new_credit_id,amount_in_12_months,amount_in_6_months,amount_in_18_months,last_update_time_stamp,fiscal_code_fk)"
        value_attr = "VALUES(%s,%s,%s,%s,%s,%s)"
        values = (
            mix_credit_id, dict_data['amount_in_12_months'], dict_data['amount_in_6_months'],
            dict_data['amount_in_18_months'],
            datetime.datetime.now(), dict_data['fiscal_code'])
        try:
            cursor.execute(insert_query + value_attr, values)
            print(cursor.rowcount, "was inserted.")
        except mysql.connector.errors.IntegrityError:
            print("Duplicated key not inserted")
        print(cursor.rowcount, "was inserted.")
        connection.commit()


def send_credit_mix(dict_data: dict, cursor, connection):
    # send_person_data(dict_data,cursor,connection)
    tag = True
    mix_credit_id = 0
    query = 'SELECT MAX(credit_mix_id) FROM credit_mix'
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        mix_credit_id = row[0]
    if (tag):
        if (mix_credit_id == None):
            mix_credit_id = 0
        else:
            mix_credit_id += 1
    if (find_fk(dict_data, cursor, connection) == False):
        insert_query = "INSERT INTO credit_mix(credit_mix_id,installment,house_mortgage,credit_card_number,last_update_time_stamp,fiscal_code_fk)"
        value_attr = "VALUES(%s,%s,%s,%s,%s,%s)"
        values = (mix_credit_id, 'yes', dict_data['house_mortgage'], dict_data['credit_card_number'],
                  datetime.datetime.now(),
                  dict_data['fiscal_code'])

        cursor.execute(insert_query + value_attr, values)
        print(cursor.rowcount, "was inserted.")
        connection.commit()


def send_assets_data(dict_data: dict, cursor, connection):
    # send_person_data(dict_data,cursor,connection)
    tag = True
    query = 'SELECT MAX(asset_id) FROM assets'
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        asset_id = row[0]
    if (tag):
        if asset_id is None:
            asset_id = 0
        else:
            asset_id += 1
    if not find_fk(dict_data, cursor, connection):
        insert_query = "INSERT INTO assets(asset_id,total_amount_of_house,monthly_income,savings,other_savings,last_updated_time_stamp,fiscal_code_fk)"
        value_attr = "VALUES(%s,%s,%s,%s,%s,%s,%s)"
        values = (
            asset_id, dict_data['total_house_amount'], dict_data['monthly_income'], dict_data['savings'],
            dict_data['other_savings'],
            datetime.datetime.now(), dict_data['fiscal_code'])
        cursor.execute(insert_query + value_attr, values)
        print(cursor.rowcount, "was inserted.")
        connection.commit()


def send_losses_data(dict_data: dict, cursor, connection):
    # send_person_data(dict_data,cursor,connection)
    tag = True
    query = 'SELECT MAX(losses_id) FROM losses'
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        losses_id = row[0]
    if tag:
        if losses_id is None:
            losses_id = 0
        else:
            losses_id += 1
    if not find_fk(dict_data, cursor, connection):
        insert_query = "INSERT INTO losses(losses_id,actual_debit_credit_cards,amount_due_mortgage,last_update_time_stamp,fiscal_code_fk)"
        value_attr = "VALUES(%s,%s,%s,%s,%s)"
        values = (
            losses_id, dict_data['actual_debit_credit_cards'], dict_data['amount_due_mortgage'], datetime.datetime.now(),
            dict_data['fiscal_code'])
        cursor.execute(insert_query + value_attr, values)
        print(cursor.rowcount, "was inserted.")
        connection.commit()


def send_bank_data(dict_data: dict, cursor, connection):
    tag = True
    check_data = True
    # check first if the data has been there already
    query = 'SELECT * FROM bank_data'
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        if str(row[1]) == dict_data['bank_name'] and str(row[2]) == dict_data['bank_country']:
            check_data = False
    if check_data:
        ## now if not there then send the data
        query = 'SELECT MAX(bank_data_id) FROM bank_data'
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        for row in data:
            bank_id = row[0]
        if (tag):
            if (bank_id == None):
                bank_id = 0
            else:
                bank_id += 1
        print(bank_id)
        if (find_fk(dict_data, cursor, connection) == False):
            ## first add bank data
            insert_query = "INSERT INTO bank_data(bank_data_id,bank_name,bank_country)"
            value_attr = "VALUES(%s,%s,%s)"
            values = (bank_id, dict_data['bank_name'], dict_data['bank_country'])
            cursor.execute(insert_query + value_attr, values)
            print(cursor.rowcount, "was inserted.")
            connection.commit()

            ## add personal relation of person and bank
        query = 'SELECT MAX(bank_person_relationships_id) FROM 	bank_person_relationships'
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        for row in data:
            p_id = row[0]
        if (tag):
            if (p_id == None):
                p_id = 0
            else:
                p_id += 1
        if (find_fk(dict_data, cursor, connection) == False):
            ## first add bank data
            insert_query = "INSERT INTO bank_person_relationships(bank_person_relationships_id,bank_id,person_id,last_update_time_stamp)"
            value_attr = "VALUES(%s,%s,%s,%s)"
            values = (p_id, bank_id, dict_data['fiscal_code'], datetime.datetime.now())
            cursor.execute(insert_query + value_attr, values)
            print(cursor.rowcount, "was inserted.")
            connection.commit()


## main
def main(r: redis.StrictRedis):
    keys_to_delete = list()
    t = get_dicts_from_redis('new_credit')
    if t[0] == False:
        print("No new new_credit data")
        new_credit_dicts = []
    else:
        new_credit_dicts = t[0]
        keys_to_delete += t[1]
    t = get_dicts_from_redis('credit_mix')
    if t[0] == False:
        print("No new credit_mix data")
        credit_mix_dicts = []
    else:
        credit_mix_dicts = t[0]
        keys_to_delete += t[1]
    t = get_dicts_from_redis('assets')
    if t[0] == False:
        print("No new assets data")
        assets_dicts = []
    else:
        assets_dicts = t[0]
        keys_to_delete += t[1]
    t = get_dicts_from_redis('losses')
    if t[0] == False:
        print("No new losses data")
        losses_dicts = []
    else:
        losses_dicts = t[0]
        keys_to_delete += t[1]
    t = get_dicts_from_redis('bank')
    if t[0] == False:
        print("No new bank data")
        bank_dicts = []
    else:
        bank_dicts = t[0]
        keys_to_delete += t[1]

    (cursor, connection) = connect_db()
    for bank_dict in bank_dicts:
        send_bank_data(bank_dict, cursor, connection)
    for new_credit_dict in new_credit_dicts:
        send_new_credit(new_credit_dict, cursor, connection)
    for credit_mix_dict in credit_mix_dicts:
        send_credit_mix(credit_mix_dict, cursor, connection)
    for assets_dict in assets_dicts:
        send_assets_data(assets_dict, cursor, connection)
    for losses_dict in losses_dicts:
        send_losses_data(losses_dict, cursor, connection)
    close_db_connection(connection, cursor)
    if keys_to_delete:
        r.delete(*keys_to_delete)
