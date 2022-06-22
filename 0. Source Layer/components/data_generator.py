import os
import sys

import pandas as pd
import random
from random import randint
import uuid

import datetime
import re



def Generate():
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the root dir
    temp = []
    fiscale = []
    users = []

    def getBankData():
        banks = pd.read_excel("./datasets/top100banks2017-12-31.xlsx")
        bankNames = banks['bank']
        bankCountries = banks['country']

    def personalData():
        fnames = pd.read_csv('./datasets/fname.csv')
        lnames = pd.read_csv('./datasets/lname.csv')
        fnames = list(fnames['fname'])
        lnames = list(lnames['lname'])
        for i in range(0, 160000):
            ## Random date
            start_date = datetime.date(1960, 1, 1)
            end_date = datetime.date(1997, 2, 1)
            time_between_dates = end_date - start_date
            days_between_dates = time_between_dates.days
            random_number_of_days = random.randrange(days_between_dates)
            random_date = start_date + datetime.timedelta(days=random_number_of_days)
            temp = []
            sex = random.choice(['Female', 'Male'])
            dob = str(random_date)
            findex = randint(1, len(fnames) - 1)
            lindex = randint(1, len(lnames) - 1)
            ethnicity = ['white', 'black', 'asian', 'afro-american', 'mix', 'caribbean', 'native american']
            ethnixity_i = randint(0, 6)
            education = ['no diploma', 'primary school', 'middle school', 'high school', 'bachelor', 'master', 'phd']
            education_i = randint(0, 6)
            purpose = ''
            phone_number = phone_numbers
            email = fnames[findex] + '_' + lnames[lindex] + '@gmail.com'
            temp.append(fiscale[i])
            temp.append(fnames[findex])
            temp.append(lnames[lindex])
            temp.append(sex)
            temp.append(dob)
            temp.append(ethnicity[ethnixity_i])
            temp.append(education[education_i])
            temp.append(purpose)
            temp.append(phone_number[i])
            temp.append(email)

            users.append(temp)

        users_information = pd.DataFrame(data=users,
                                         columns=['Id Number', 'first name', 'last name', 'sex', 'DOB', 'ethnicity',
                                                  'education', 'purpose', 'phone number', 'email'])
        users_information.to_csv('user_information.csv')

    def companyData():
        companyNames = pd.read_excel(root+'/assets/0. Source Data/datasets/company.xlsx')
        country = companyNames['COUNTRY']
        names = companyNames['COMPANY']
        market = companyNames['MARKET']
        exrt = ['reach', 'hr', 'headquarters', 'enquiries', 'info', 'sales', 'marketing', 'contact']
        for i in range(1, 1345):
            ## Random date
            start_date = datetime.date(1960, 1, 1)
            end_date = datetime.date(1997, 2, 1)
            time_between_dates = end_date - start_date
            days_between_dates = time_between_dates.days
            random_number_of_days = random.randrange(days_between_dates)
            random_date = start_date + datetime.timedelta(days=random_number_of_days)
            temp = []
            dob = str(random_date)
            cindex = randint(1, len(names) - 1)
            exrt_i = randint(0, 7)
            name = re.sub('[^A-Za-z0-9]+', '', str(names[cindex]))
            if str(name).endswith('.'):
                email = exrt[exrt_i] + '@' + ''.join(map(str.lower, str(name).split())) + 'org'
            else:
                email = exrt[exrt_i] + '@' + ''.join(map(str.lower, str(name).split())) + '.org'

            employee = randint(5, 50)
            purpose = ''
            phone_number = phone_numbers
            temp.append(fiscale[cindex])
            temp.append(names[cindex])
            temp.append(dob)
            temp.append(country[cindex])
            temp.append(employee)
            temp.append(purpose)
            temp.append(phone_number[cindex])
            temp.append(email)

            users.append(temp)

        users_information = pd.DataFrame(data=users,
                                         columns=['registration number', 'name', 'established date', 'country',
                                                  'number of employs', 'purpose', 'phone number', 'email'])
        users_information.to_csv('company_information.csv')

    def random_phone_num_generator():
        first = str(random.randint(100, 999))
        second = str(random.randint(1, 888)).zfill(3)
        last = (str(random.randint(1, 9998)).zfill(4))
        while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
            last = (str(random.randint(1, 9998)).zfill(4))
        return '{}-{}-{}'.format(first, second, last)

    phone_numbers = []
    # getBankData()
    for i in range(0, 1345):
        ph_no = []
        id = uuid.uuid4()
        fiscale.append(str(id))
        phone_numbers.append(random_phone_num_generator())

    ## function
    # personalData()
    companyData()
