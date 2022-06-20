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

class HTML:

    def __init__(self,data, bank):
        self.data = data
        self.bank = bank

    def to_html(data,bank):
        banksName = str(bank['names'])
        data['bank_name'] = bank['names']
        data['bank_country'] = bank['country']
        # print(banksName)
        banksName =banksName.replace(' ','_')
        banksName = banksName.replace('/','_')
        data = pd.DataFrame(data)
        data.to_html('./reports/'+banksName+'.html')