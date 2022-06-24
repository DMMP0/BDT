import os


import pandas as pd

parentDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # finds the parent directory

class Clipboard:

    def __init__(self,data, bank):
        self.data = data
        self.bank = bank


    def to_clipboard(self,data,bank):
        # print('here')
        data = pd.DataFrame(data)
        banksName = str(bank['names'])
        data['bank_name'] = bank['names']
        data['bank_country'] = bank['country']
        banksName =banksName.replace(' ','_')
        banksName = banksName.replace('/','_')
        # print(data)
        data.to_records(parentDir+ '/reports/'+str(banksName) +'.txt')