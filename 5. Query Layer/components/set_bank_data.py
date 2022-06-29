'''this script here is to send the bank data to the 4 tables in the database, 
1. Credit mix table
2. asset
3. losses
new credit'''
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
import services.get_bank_data as bd 



def read_data(fk):
    # bank = bd.get_bank_data(fk)
    credit_mix = bd.get_credit_mix(fk)
    assets = bd.get_assets_data(fk)
    losses = bd.get_losses_data(fk)
    new_credit  =bd.get_new_credit(fk)
    print(credit_mix)
    print(assets)
    print(losses)
    print(new_credit)
    return(credit_mix,assets,losses,new_credit)





read_data('81804c59-627e-4a5d-9a91-87d6eb3a705c')