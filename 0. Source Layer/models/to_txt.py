import os
import re
import pandas as pd
import random
from random import randint
import ccard

source = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # finds the 0. Data Source directory

currentDir = source + '/components'
val = 30000.00
purpose = ['prototype', 'marketing', 'validation', 'scale-up', 'industrial equipment', 'office', 'employee',
           'other investment']


class RTF:
    def __init__(self):
        self.data = []
        self.bank = []

    def clean(self):
        self.data = []
        self.bank = []

    def set_data(self, data):
        self.data = data

    def set_bank(self, bank):
        self.bank = bank

    def create_bank_data(self, bdata):
        bank_data = bdata
        banksName = str(self.bank[0])
        banksName = banksName.replace(' ', '_')
        banksName = banksName.replace('/', '_')
        bank_data = pd.DataFrame(bank_data)
        bank_data['bank_name'] = self.bank[0]
        bank_data['bank_country'] = self.bank[1]
        bank_data['open_new_credit_in_6_months'] = 0
        bank_data['ammount_in_6_months'] = 0.00
        bank_data['new_credit_in_12_months'] = 0.00
        bank_data['new_credit_in_18_months'] = 0.00
        bank_data['ammount_in_12_months'] = 0.00
        bank_data['ammount_in_18_months'] = 0.00
        bank_data['house_mortage'] = 1
        bank_data['amount_of_house_mortage'] = 0.00
        bank_data['amount_duee_mortage'] = 0.00
        bank_data['house_property'] = 00
        bank_data['total_house_amount'] = 0.00
        bank_data['credit_card_number'] = 0
        bank_data['credit_card_limit_total'] = 0
        bank_data['actual_debit_credit_cards'] = 0.00
        bank_data['monthly_income'] = 0.00
        bank_data['savings'] = 0.00
        bank_data['other_savings'] = 0.00
        return bank_data

    def create_questura_data(self, questuradata) -> any:
        questura_data = questuradata
        # print(bank['names'])
        # print(self.bank[0])

        # bank = pd.DataFrame(bank)
        # bank = pd.DataFrame(data = bank.values , columns=bank.columns)
        # bank = list(bank)
        # print(bank)
        banksName = str(self.bank[0])
        banksName = banksName.replace(' ', '_')
        banksName = banksName.replace('/', '_')
        questura_data = pd.DataFrame(questura_data)
        questura_data['questura_country'] = self.bank[1]
        questura_data['bankruptcy'] = bool
        questura_data['inscred'] = "${:,.2f}".format(val + random.randint(5000, 10000000))
        questura_data['fraudis'] = bool
        questura_data['investegation'] = bool
        questura_data['accused'] = bool
        questura_data['condamned'] = bool
        questura_data['civ_pass'] = bool

        return questura_data

    def create_risk_broker_data(self, data) -> any:
        broker_data = data
        banksName = str(self.bank[0])
        banksName = banksName.replace(' ', '_')
        banksName = banksName.replace('/', '_')
        broker_data = pd.DataFrame(broker_data)
        broker_data['agency_country'] = self.bank[1]
        broker_data['agency_name'] = ''
        broker_data['from30to60'] = random.choice([0,0,0,0,0,0,0,0,0,1])
        broker_data['from60to90'] = random.choice([0,0,0,0,0,0,0,0,0,1])
        broker_data['morethan90'] = random.choice([0,0,0,0,0,0,0,0,0,1])
        broker_data['debit_id'] =''
        broker_data['insolvent'] = bool
        broker_data['insolvent_ammount'] = "$0.00"

        return broker_data

    def police_rtf(self):
        questura_data = pd.DataFrame(self.data)
        banksName = self.bank['names']
        # questura_data['bank_name'] = self.bank['names']
        # questura_data['bank_country'] = self.bank['country']
        # print(banksName)

        banksName = self.bank['names']
        banksName = re.sub('[^a-zA-Z0-9 \n\.]', '', banksName)
        questura_data = self.create_questura_data(questura_data)
        questura_data = pd.DataFrame(questura_data)
        # print(banksName)
        for index, item in questura_data.iterrows():
            questura_data = pd.DataFrame(questura_data)
            questura_data.loc[index, 'questura_country'] = self.bank[1]
            questura_data.loc[index,'bankruptcy'] = random.choice([True, False, False, False, False, False, False, False, False, False])
	    if(questura_data.loc[index,'bankruptcy'] == True):
	   	 questura_data.loc[index,'inscred'] = "${:,.2f}".format(val + random.randint(5000,10000000))
	    if(questura_data.loc[index,'bankruptcy'] == False):
	    	 questura_data.loc[index,'fraudis'] = False
	    else: 
		 questura_data.loc[index,'fraudis'] = random.choice([True, False, False, False, False, False, False, False, False, False])
	    questura_data.loc[index,'investegation'] = random.choice([True, False, False, False, False, False, False, False, False, False])
	    questura_data.loc[index,'accused'] = random.choice([True, False, False, False, False, False, False, False, False, False])
	    questura_data.loc[index,'condamned'] = random.choice([True, False, False, False, False, False, False, False, False, False])
	    questura_data.loc[index,'civ_pass'] = random.choice([True, False, False, False, False, False, False, False, False, False])
        # print(questura_data.columns)
        with open(currentDir+'/reports/' + banksName + '_report(Questura).txt', 'a', encoding='utf-8') as f:
            questura_data = pd.DataFrame(questura_data)
            # business_data= business_data.decode('utf-8')
            questura_data.to_csv(f, index=None, sep='\t', mode='a')

    def bank_rtf(self):
        # print(self.data)
        tempData = self.data
        bank_data = pd.DataFrame(tempData)
        # bank = pd.DataFrame(bank)
        ## read in the text as a string
        # print(bank)
        banksName = self.bank['names']
        banksName = self.bank['names']
        banksName = re.sub('[^a-zA-Z0-9 \n\.]', '', banksName)
        bank_data = self.create_bank_data(bank_data)
        bank_data = pd.DataFrame(bank_data)

        # print(banksName)
        for index, item in bank_data.iterrows():
		    six_month_total = 0
		    twelve_month_total = 0
		    eighteen_month_total = 0
		    bank_data.loc[index,'open_new_credit_in_6_months'] = random.choice([0,0,0,0,0,0,0,0,0,1])
		    if bank_data.loc[index,'open_new_credit_in_6_months'] == 1:
			   six_month_total = val + random.randint(2000,10000)
		    bank_data.loc[index,'ammount_in_6_months'] = "${:,.2f}".format(six_month_total)
		    bank_data.loc[index,'new_credit_in_12_months'] = random.choice([0,0,0,0,0,0,0,0,0,1])
		    if bank_data.loc[index,'new_credit_in_12_months'] == 1:
			   twelve_month_total = six_month_total + val + random.randint(2000,10000)
		    bank_data.loc[index,'new_credit_in_18_months'] = random.choice([0,0,0,0,0,0,0,0,0,1])
		    if bank_data.loc[index,'new_credit_in_18_months'] == 1:
			   eighteen_month_total = twelve_month_total + val + random.randint(2000,10000)
		    bank_data.loc[index,'ammount_in_12_months'] = "${:,.2f}".format(twelve_month_total)
		    bank_data.loc[index,'ammount_in_18_months'] = "${:,.2f}".format(eighteen_month_total)
		    bank_data.loc[index,'house_mortage'] = random.choice([True, False])
		    if(bank_data.loc[index,'house_mortage'] == True):
			   max_mortgage = val + random.randint(50000,500000)
			   bank_data.loc[index,'amount_of_house_mortage'] = "${:,.2f}".format(max_mortgage)
			   bank_data.loc[index,'amount_duee_mortage'] ="${:,.2f}".format(val  + random.randint(50000,max_mortgage))
			   bank_data.loc[index,'house_property'] = True
		    else:
			   bank_data.loc[index,'house_property'] = random.choice([True, False])	
		    if(bank_data.loc[index,'house_property'] is True):
			 bank_data.loc[index,'total_house_amount'] ="${:,.2f}".format(val + random.randint(50000,500000))
		    number_credit_cards = random.randint(1,5)
		    bank_data.loc[index,'credit_card_number'] = number_credit_cards
		    max_credit_credit_card = number_credit_cards*random.randint(1000,4000)
		    bank_data.loc[index,'credit_card_limit_total'] = max_credit_credit_card
		    bank_data.loc[index,'actual_debit_credit_cards'] = random.randint(1000,max_credit_credit_card)
		    bank_data.loc[index,'monthly_income'] ="${:,.2f}".format(val + random.randint(0,5000))
		    bank_data.loc[index,'savings'] = "${:,.2f}".format(val + random.randint(200,100000))
		    bank_data.loc[index,'other_savings']= "${:,.2f}".format(val + random.randint(100,20000))
        with open(currentDir+'/reports/' + banksName + '_report(Bank).txt', 'a', encoding='utf-8') as f:
            bank_data = pd.DataFrame(bank_data)
            # business_data= business_data.decode('utf-8')
            bank_data.to_csv(f, index=None, sep='\t', mode='a')

    agencey_names = ['CRIF', 'CTC', 'Banca d italia', 'experian']

    def broker_rtf(self):
        broker_data = pd.DataFrame(self.data)
        banksName = self.bank['names']
        banksName = re.sub('[^a-zA-Z0-9 \n\.]', '', banksName)
        broker_data = self.create_risk_broker_data(broker_data)

        broker_data = pd.DataFrame(broker_data)
        # print(banksName)
        for index, item in broker_data.iterrows():
            broker_data = pd.DataFrame(broker_data)
	    broker_data.loc[index, 'agency_name'] = self.agencey_names[(randint(0, 3))]
            broker_data.loc[index, 'agency_country'] = self.bank[1]
	    broker_data['from30to60'] = random.choice([0,0,0,0,0,0,0,0,0,1])
	    broker_data['from60to90'] = random.choice([0,0,0,0,0,0,0,0,0,1])
	    broker_data['morethan90'] = random.choice([0,0,0,0,0,0,0,0,0,1])
	    broker_data.loc[index, 'debit_id'] = str(ccard.mastercard())
	    broker_data.loc[index, 'insolvent'] = random.choice([True, False, False, False, False, False, False, False, False, False])
	           if broker_data.loc[index, 'insolvent'] == True:
		           broker_data.loc[index, 'insolvent_ammount'] = "${:,.2f}".format(val + random.randint(5000, 20000))
        with open(currentDir+'/reports/' + banksName + '_report(Broker).txt', 'a', encoding='utf-8') as f:
            broker_data = pd.DataFrame(broker_data)
            # business_data= business_data.decode('utf-8')
            broker_data.to_csv(f, index=None, sep='\t', mode='a')
