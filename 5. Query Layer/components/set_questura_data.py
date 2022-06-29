
from asyncio.windows_events import NULL
from matplotlib.font_manager import json_dump
from mysql.connector import Error
import sys,os
import json
import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # finds the current directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the parent directory
from models.bank import Bank
from models.broker import Broker
from models.questura import Questura
from models.statement import Statement
from models.person_info import Person
import services.get_questura_data as bd 
import operator



def read_data(fk):
    # bank = bd.get_bank_data(fk)
    dict = {'0':0, '1':0 , '2':0}
    criminal_records = bd.get_criminal_data(fk)
    print(criminal_records)
    for rows in criminal_records:
        if(rows[0] == 0):
            val = dict.get('0')
            val+=1
            temp = {'0': val}
            dict.update(temp)
        if(rows[0] == 1):
            val = dict.get('1')
            val+=1
            temp = {'1': val}
            dict.update(temp)
        if(rows[0] == 2):
            val = dict.get('2')
            val+=1
            temp = {'2': val}
            dict.update(temp)

    bankrupcy = max(dict, key=dict.get)
    return bankrupcy

