from unicodedata import name
from xmlrpc.client import DateTime
import pandas as pd
import random
from random import randint
import uuid
import numpy as np
import datetime
import docx
import re
import os

from docx.shared import Pt, Mm

class RTF:

    def __init__(self,data, bank):
        self.data = data
        self.bank = bank

    
    def to_rtf(data,bank):
        data = pd.DataFrame(data)
        # bank = pd.DataFrame(bank)
        ## read in the text as a string
        # print(bank)
        banksName = bank['names']
        data['bank_name'] = bank['names']
        data['bank_country'] = bank['country']
        # print(banksName)
        banksName =banksName.replace(' ','_')
        banksName = banksName.replace('/','_')
        # print(data)
        with open('./reports/'+str(banksName)+'_report.txt', 'a',encoding='utf-8') as f:
            data = pd.DataFrame(data)
            # business_data= business_data.decode('utf-8')
            data.to_csv(f,index=None, sep='\t', mode='a')