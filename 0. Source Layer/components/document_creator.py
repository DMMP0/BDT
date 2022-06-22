import os
from xmlrpc.client import DateTime
import pandas as pd
import random
from random import randint

import numpy as np
import sys


from models.to_txt import RTF
from models.to_word import Word
from models.to_tex import Tex
from models.to_clipboard import Clipboard
from models.to_excel import Excel
from models.to_html import HTML
# function
import modulefinder
from docx.shared import Pt, Mm

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the root directory

def create_documents():
    global root
    threshold = 50  # this is the number of companies request for the bank data

    business_data = pd.read_csv(root+'/assests/0. Source Data/credit data/company_information.csv')
    personal_data = pd.read_csv(root+'/assests/0. Source Data/credit data/user_information.csv')
    bank_data = pd.read_excel(root+'/assests/0. Source Data/credit data/banks.xlsx')
    # bank_data.drop(columns=bank_data.columns[0], axis=1, inplace=True)
    business_data = pd.DataFrame(data=business_data, columns=business_data.columns)
    personal_data = pd.DataFrame(data=personal_data, columns=personal_data.columns)
    purpose = ['prototype', 'marketing', 'validation', 'scale-up', 'industrial equipment', 'office', 'employee',
               'other investment']

    def update_header(data) -> list:
        temp = []
        data = pd.DataFrame(data)
        columns = data.columns
        for column in columns:
            column = str(column).replace(' ', '_')
            temp.append(column)
        return temp

    def data_cleaning_for_classes(obj, df, bank):
        obj.set_data(df)
        obj.set_bank(bank)

    def update_header_of_data():
        business_data.columns = update_header(business_data)
        personal_data.columns = update_header(personal_data)
        bank_data.columns = update_header(bank_data)

    def create_RTF(rnd):
        banks = bank_data.sample(n=rnd_banks)
        banks = pd.DataFrame(banks)
        for index, bank in banks.iterrows():
            rnd = randint(2, rnd)
            rand = np.random.permutation(len(data))[:rnd]
            df = data.take(rand)

            obj1 = RTF()
            obj1.set_data(df)
            obj1.set_bank(bank)
            obj1.police_rtf()
            obj1.clean()

            df = data.take(rand)
            obj2 = RTF()
            obj2.set_data(df)
            obj2.set_bank(bank)
            obj2.bank_rtf()
            obj2.clean()

            df = data.take(rand)
            obj3 = RTF()
            obj3.set_data(df)
            obj3.set_bank(bank)
            obj3.broker_rtf()
            obj3.clean()
        print(rnd)

    def create_Word(rnd):
        banks = bank_data.sample(n=rnd_banks)
        banks = pd.DataFrame(banks)
        for index, bank in banks.iterrows():
            rnd = randint(2, rnd)
            rand = np.random.permutation(len(data))[:rnd]
            df = data.take(rand)

            obj1 = Word()
            obj1.set_data(df)
            obj1.set_bank(bank)
            obj1.police_to_word()
            obj1.clean()
            df = data.take(rand)
            obj2 = Word()
            obj2.set_data(df)
            obj2.set_bank(bank)
            obj2.bank_to_word()
            obj2.clean()
            df = data.take(rand)
            obj3 = Word()
            obj3.set_data(df)
            obj3.set_bank(bank)
            obj3.broker_to_word()
            obj3.clean()
        print(idx)

    def create_HTML(rnd):
        banks = bank_data.sample(n=rnd_banks)
        banks = pd.DataFrame(banks)
        for index, bank in banks.iterrows():
            rnd = randint(2, rnd)
            rand = np.random.permutation(len(data))[:rnd]
            df = data.take(rand)

            obj1 = HTML()
            obj1.set_data(df)
            obj1.set_bank(bank)
            obj1.police_html()
            obj1.clean()
            df = data.take(rand)
            obj2 = HTML()
            obj2.set_data(df)
            obj2.set_bank(bank)
            obj2.bank_html()
            obj2.clean()
            df = data.take(rand)
            obj3 = HTML()
            obj3.set_data(df)
            obj3.set_bank(bank)
            obj3.broker_html()
            obj3.clean()
        print(idx)

    def create_Excel(rnd):
        banks = bank_data.sample(n=rnd_banks)
        banks = pd.DataFrame(banks)
        for index, bank in banks.iterrows():
            rnd = randint(2, rnd)
            rand = np.random.permutation(len(data))[:rnd]
            df = data.take(rand)
            obj1 = Excel()
            obj1.set_data(df)
            obj1.set_bank(bank)
            obj1.police_excel()
            obj1.clean()

            df = data.take(rand)
            obj2 = Excel()
            obj2.set_data(df)
            obj2.set_bank(bank)
            obj2.bank_excel()
            obj2.clean()

            df = data.take(rand)
            obj3 = Excel()
            obj3.set_data(df)
            obj3.set_bank(bank)
            obj3.broker_excel()
            obj3.clean()
        print(idx)

    # Main
    update_header_of_data()
    for i in range(0, 4):
        data = business_data.iloc[0:threshold]
        data['purpose'] = purpose[(randint(0, 7))]
        rnd = randint(10, threshold)
        idx = rnd
        rnd_banks = randint(5, idx)
        print("Random number", rnd)
        if i == 0:
            create_RTF(rnd)
        if i == 1:
            create_Word(rnd)
        if i == 2:
            create_HTML(rnd)
        if i == 3:
            create_Excel(rnd)
