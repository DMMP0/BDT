import os
import pandas as pd
import re
from random import randint
import datetime as dt
import numpy as np
import sys
from datetime import date, datetime
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the parent directory
from models.to_txt import RTF
from models.to_word import Word

from models.to_excel import Excel
from models.to_html import HTML

## Public variables

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the root dir
currentDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
threshold = 1000  # this is the number of companies request for the bank data

business_data = pd.read_csv(parentDir + '/assets/credit data/company_information.csv')
personal_data = pd.read_csv(parentDir + '/assets/credit data/user_information.csv')
bank_data = pd.read_excel(parentDir + '/assets/credit data/banks.xlsx')
# bank_data.drop(columns=bank_data.columns[0], axis=1, inplace=True)
business_data = pd.DataFrame(data=business_data, columns=business_data.columns)
personal_data = pd.DataFrame(data=personal_data, columns=personal_data.columns)
purpose = ['prototype', 'marketing', 'validation', 'scale-up', 'industrial equipment', 'office', 'employee',
           'other investment']
unique_companies = []
unique_partners = []

data = business_data
person_data = personal_data
declaration_data = []


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

def create_RTF(data, rnd):
        banks = bank_data.sample(n=randint(1,2))
        banks = pd.DataFrame(banks)
        for index, bank in banks.iterrows():
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
        # print(rnd)

def create_Word(data, rnd):
        banks = bank_data.sample(n=randint(1,2))
        banks = pd.DataFrame(banks)
        for index, bank in banks.iterrows():
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
        # print(idx)

def create_HTML(data, rnd):
        banks = bank_data.sample(n=randint(1,2))
        banks = pd.DataFrame(banks)
        for index, bank in banks.iterrows():
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
        # print(idx)

def create_Excel(data, rnd):
        banks = bank_data.sample(n=randint(1,2))
        banks = pd.DataFrame(banks)
        for index, bank in banks.iterrows():
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
        # print(idx)

def declaration_file():
        for i in range(0,5):
            no_of_partners = randint(2, 5)
            company_partners = person_data.sample(n=no_of_partners)
            # print(company_partners)
            have_them = company_partners[company_partners['Id_Number'].isin(unique_partners)]
            # print(have_them)
            if (have_them.empty is True):
                # print('Unique found')
                unique_partners.append(list(company_partners['Id_Number']))
                company_partners['purpose'] = purpose[(randint(0, 7))]
                company = data.sample(n=1)
                have_company = company[company['registeration_number'].isin(unique_companies)]
                if (have_company.empty is True):
                    # print(company.values.flatten().tolist())
                    unique_companies.append(company['registeration_number'])
                    company = company.values.flatten().tolist()
                    # company = list(company)
                    # print(list(company['name']))
                    company_partners['registeration_number'] = company[0]
                    company_partners['company_name'] = company[1]
                    company_partners['establied_date'] = company[2]
                    company_partners['country'] = company[3]
                    company_partners['number_of_employes'] = company[4]
                    company_partners['phone_number'] = company[5]
                    company_partners['email'] = company[6]
                    company_partners['amount_of_credit'] = "${:,.2f}".format(random.randint(5000,100000000000))
                    company_partners['duration_in_months'] = random.randint(6,20)
                    company_partners = pd.DataFrame(company_partners)
                    # print(company_partners)
                    company_name = company[1]
                    company_name = re.sub('[^a-zA-Z0-9 \n\.]', '', company_name)
                    company_partners.to_csv(currentDir+'/reports/' + str(company_name) + '(Declaration).csv')

                    # declaration_data.append(company_partners)

        clients = [item for sublist in unique_partners for item in sublist]
        # print(clients)
        clients = pd.DataFrame(clients, columns=['Fiscal Code'])
        clients.loc[:,'Date and Time'] = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        
        return clients
        # with open('list.csv', 'w') as f:

        #     # using csv.writer method from CSV package
        #     write = writer(f)

        #     write.writerow(clients)


import csv


def work():
    update_header_of_data()
    # print('Imhere')
    name = '0.Client_List'
    tag = True
    new_clients = declaration_file()

    with open('0.Client_List.csv', 'r') as csvfile:
        csv_dict = [row for row in csv.DictReader(csvfile)]
        if len(csv_dict) == 0:
            tag = False

    if (tag):
        client = pd.read_csv(name + '.csv')
        client = pd.concat([client, new_clients], ignore_index=True)
        client.to_csv(name + '.csv')
    else:
        new_clients.to_csv(name + '.csv')

    clients = pd.read_csv(name + '.csv')
    client_full_data = personal_data[personal_data['Id_Number'].isin(new_clients['Fiscal Code'])]
    for i in range(0, 4):

        rnd = randint(2, len(new_clients))
        idx = rnd
        # rnd_banks = randint(5, idx)
        # print("Random number", rnd)
        if i == 0:
            create_RTF(client_full_data, rnd)
        if i == 1:
            create_Word(client_full_data, rnd)
        if i == 2:
            create_HTML(client_full_data, rnd)
        if i == 3:
            create_Excel(client_full_data, rnd)
