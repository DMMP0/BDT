

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
import services.get_personal_data as bd 



def read_data(fk):
    person = bd.get_person_data(fk)
    print("Getting personal Data" , person)
    return person


# read_data('81804c59-627e-4a5d-9a91-87d6eb3a705c')