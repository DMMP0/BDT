'''this script here is to send the personal data to the personal information table'''

from matplotlib.font_manager import json_dump
import mysql.connector
from mysql.connector import Error
import sys,os
import json
import datetime

# curr = os.path.dirname(os.path.curdir)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the parent directory

def connect_db():
    config_db = json.loads(os.environ['CREDENTIALS'])
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




def get_criminal_data(key):
    # send_person_data(dict_data,cursor,connection)
    (cursor,connection) = connect_db()
    query = 'SELECT MAX(last_updated_time_stamp) FROM criminal_records where fiscal_code_fk = %s'
    val = (key,)
    cursor = connection.cursor()
    cursor.execute(query,val)
    data = cursor.fetchall()
    for row in data:
        date = row[0]
    query = 'SELECT bankrupty FROM criminal_records where fiscal_code_fk = %s and last_updated_time_stamp = %s'
    val = (key,date)
    cursor.execute(query,val)
    if (cursor.description is None):
        return []
    else:
        data = cursor.fetchall()
        close_db_connection(connection,cursor)
        return data
## main


