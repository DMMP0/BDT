import pandas as pd
import random
from random import randint
import numpy as np
import ccard
import docx

from docx.shared import Pt, Mm

val  = 30000.00
purpose = ['prototype', 'marketing', 'validation', 'scale-up', 'industrial equipment', 'office', 'employee', 'other investment']
def bank_data(data,bank)->any:
        # print(bank['names'])
        print(bank[0])
        
        # bank = pd.DataFrame(bank)
        # bank = pd.DataFrame(data = bank.values , columns=bank.columns)
        # bank = list(bank)
        # print(bank)
        banksName = str(bank[0])
        banksName =banksName.replace(' ','_')
        banksName = banksName.replace('/','_')
        data = pd.DataFrame(data)
        data['bank_name'] = bank[0]
        data['bank_country'] = bank[1]
        data['open_new_credit_in_6_months'] = 0
        data['ammount_in_6_months'] = 0.00
        data['new_credit_in_12_months'] = 0.00
        data['new_credit_in_18_months'] = 0.00
        data['ammount_in_12_months'] = 0.00
        data['ammount_in_18_months'] = 0.00
        data['house_mortage'] = 1
        data['amount_of_house_mortage'] = 0.00
        data['amount_duee_mortage'] = 0.00
        data['house_property'] = 00
        data['total_house_amount'] =0.00
        data['credit_card_number'] = 0
        data['actual_debit_credit_cards'] =0.00
        data['monthly_income'] = 0.00
        data['savings'] = 0.00
        data['other_savings']= 0.00
        return data

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
        data =  bank_data(data,bank)
        banksName = str(bank[0])
        banksName =banksName.replace(' ','_')
        banksName = banksName.replace('/','_')
        data = pd.DataFrame(data)
        # print(banksName)
        for index,item in data.iterrows():
            
            data.loc[index,'purpose'] = purpose[(randint(0,7))] 
            data.loc[index,'open_new_credit_in_6_months'] = random.randint(0,10)
            data.loc[index,'ammount_in_6_months'] = "${:,.2f}".format(val + random.randint(5000,100000000000))
            data.loc[index,'new_credit_in_12_months'] = random.randint(0,10)
            data.loc[index,'new_credit_in_18_months'] = random.randint(0,10)
            data.loc[index,'ammount_in_12_months'] ="${:,.2f}".format(val + random.randint(5000,100000000000))
            data.loc[index,'ammount_in_18_months'] = "${:,.2f}".format(val + random.randint(5000,100000000000))
            data.loc[index,'house_mortage'] = random.randint(1,10)
            data.loc[index,'amount_of_house_mortage'] ="${:,.2f}".format(val + random.randint(5000,100000000000))
            data.loc[index,'amount_duee_mortage'] =  val  + random.randint(5000,100000000000)
            data.loc[index,'house_property'] = random.randint(0,10)
            data.loc[index,'total_house_amount'] ="${:,.2f}".format(val + random.randint(5000,100000000000))
            data.loc[index,'credit_card_number'] = str(ccard.visa())
            data.loc[index,'actual_debit_credit_cards'] = random.randint(2,10)
            data.loc[index,'monthly_income'] ="${:,.2f}".format(val + random.randint(5000,100000000000))
            data.loc[index,'savings'] = "${:,.2f}".format(val + random.randint(5000,100000000000))
            data.loc[index,'other_savings']= "${:,.2f}".format(val + random.randint(5000,100000000000))
            # data.loc[index] = item
            print(data)
        # print(data)
        with open('./reports/'+str(banksName)+'_report.txt', 'a',encoding='utf-8') as f:
            data = pd.DataFrame(data)
            # business_data= business_data.decode('utf-8')
            data.to_csv(f,index=None, sep='\t', mode='a')