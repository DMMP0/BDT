import anvil.server
import json
import anvil.server
import mysql.connector
from mysql.connector import Error
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # finds the current directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the parent directory
current_dir = os.getcwd()
par_dir = os.path.dirname(current_dir) 
par_dir = os.path.dirname(par_dir)
sys.path.append(par_dir+'\\5. Query Layer\components')
import credit_formulation as CF



anvil.server.connect('NKBJP7OHDHIAKL4IW2C2FOWE-UZZP33BE5EVXZYOW')


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

@anvil.server.callable
def get_items(id):
    # cf.call_data_all(id)
    query = 'SELECT * FROM personal_data WHERE fiscal_code = %s'
    val =(str(id),)
    cursor.execute(query,val)
    items = cursor.fetchall()
    for item in items:
        if(item[4] == 2):
            sex = 'Male'
        else:
            sex = 'female'

    return [
        {'id': item[1], 'fname': item[2], 'lname': item[3],'dob':item[5],'phone_number':item[10],'education':item[7],'sex':sex}
        for item in items
    ]


@anvil.server.callable
def get_company_info(id):
    # cf.call_data_all(id)
    query = 'SELECT firm_registration FROM personal_data WHERE fiscal_code = %s'
    val =(str(id),)
    cursor.execute(query,val)
    items = cursor.fetchall()
    print("Items ",str(items[0]).replace("()", ""))
    query = 'SELECT * FROM firm_data WHERE registeration_number = %s'
    val =items[0]
    cursor.execute(query,val)
    items = cursor.fetchall()
    return [
        {'name': item[2], 'establish_date': item[3], 'employes': item[4],'country':item[5]}
        for item in items
    ]


@anvil.server.callable
def get_CS(id):
    return  CF.call_data_all(id)

anvil.server.wait_forever()