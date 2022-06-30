
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
import services.get_firm_data as bd 



def read_data(fk):
    # bank = bd.get_bank_data(fk)
    credit = bd.get_credit_data(fk)
    print("Getting credit Data" , credit)
    firm = bd.get_firm_data(fk)
    print("Getting firm Data" , firm)
    return (firm,credit)
