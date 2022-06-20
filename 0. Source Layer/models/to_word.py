from base64 import encode
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

class Word:

    def __init__(self,data, bank):
        self.data = data
        self.bank = bank


    def df_to_word(data,bank):
        # assert type(data) == dict, 'data has to be dict'
        doc = docx.Document()
        section = doc.sections[0]
        section.left_margin = Mm(0)
        section.right_margin = Mm(0)
        section.top_margin = Mm(10)
        section.bottom_margin = Mm(10)

        data = pd.DataFrame(data)  # My input data is in the 2D list form
        table = doc.add_table(rows=(data.shape[0]), cols=data.shape[1])  # First row are table headers!
        table.allow_autofit = True
        table.autofit = True
        banksName = str(bank['names'])
        data['bank_name'] = bank['names']
        data['bank_country'] = bank['country']
        # print(banksName)
        banksName =banksName.replace(' ','_')
        banksName = banksName.replace('/','_')
        doc = docx.Document()
        table = doc.add_table(rows = data.shape[0], cols = data.shape[1])
        table_cells = table._cells
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                 table_cells[j + i * data.shape[1]].text = str(data.values[i][j])
        doc.save(f'../components/reports/{banksName}.docx')

