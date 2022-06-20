from xmlrpc.client import DateTime
import pandas as pd
import random
from random import randint

import numpy as np
import sys

sys.path.append('../models')
from to_txt import RTF
from to_word import Word
from to_tex import Tex
from to_clipboard import Clipboard
from to_excel import Excel
from to_html import HTML
# function
import modulefinder 
from docx.shared import Pt, Mm



threshold = 50  # this is the number of companies request for the bank data

business_data = pd.read_csv('../../assests/0. Source Data/credit data/company_information.csv')
personal_data = pd.read_csv('../../assests/0. Source Data/credit data/user_information.csv')

bank_data = pd.read_excel('../../assests/0. Source Data/credit data/banks.xlsx')
# bank_data.drop(columns=bank_data.columns[0], axis=1, inplace=True)
business_data = pd.DataFrame(data=business_data, columns=business_data.columns)


def update_header(data)->list:
    temp = []
    data = pd.DataFrame(data)
    columns = data.columns
    for column in columns:
        column = str(column).replace(' ', '_')
        temp.append(column)
    return temp


business_data.columns  = update_header(business_data)
personal_data.columns  = update_header(personal_data)
bank_data.columns  = update_header(bank_data)



for i in range(0, 6):
    data = business_data.iloc[0:threshold]
    rnd = randint(10, threshold)
    idx = rnd
    rnd_banks = randint(5, idx)
    print("Random number", rnd)
    if i == 0:
        banks= bank_data.sample(n=rnd_banks)
        banks = pd.DataFrame(banks)
        for index,bank in banks.iterrows():
            rnd = randint(2, rnd)
            df = data.take(np.random.permutation(len(data))[:rnd])
            RTF.to_rtf(df,bank)
        print(rnd)
    if i == 1:
        banks= bank_data.sample(n=rnd_banks)
        banks = pd.DataFrame(banks)
        for index,bank in banks.iterrows():
            rnd = randint(2, rnd)
            df = data.take(np.random.permutation(len(data))[:rnd])
            Word.df_to_word(data[0:idx],bank)
        print(idx)
    if i == 2:
        banks= bank_data.sample(n=rnd_banks)
        banks = pd.DataFrame(banks)
        for index,bank in banks.iterrows():
            rnd = randint(2, rnd)
            df = data.take(np.random.permutation(len(data))[:rnd])
            HTML.to_html(df,bank)
        print(idx)
#     if i == 3:
#         banks= bank_data.sample(n=rnd_banks)
#         banks = pd.DataFrame(banks)
#         for index,bank in banks.iterrows():
#             rnd = randint(2, rnd)
#             df = data.take(np.random.permutation(len(data))[:rnd])
#             Tex.to_tex(df,bank)
#         print(idx)
    if i == 4:
        banks= bank_data.sample(n=rnd_banks)
        banks = pd.DataFrame(banks)
        for index,bank in banks.iterrows():
            rnd = randint(2, rnd)
            df = data.take(np.random.permutation(len(data))[:rnd])
            Excel.to_excel(df,bank)
        print(idx)
    # if i == 5:
    #     banks= bank_data.sample(n=rnd_banks)
    #     banks = pd.DataFrame(banks)
    #     for index,bank in banks.iterrows():
    #         rnd = randint(2, rnd)
    #         df = data.take(np.random.permutation(len(data))[:rnd])
    #         Clipboard.to_clipboard(df,bank)
    #     print(idx)

