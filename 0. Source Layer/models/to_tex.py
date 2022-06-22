
import pandas as pd



class Tex:

    def __init__(self,data, bank):
        self.data = data
        self.bank = bank

    
    def to_tex(data,bank):
        data = pd.DataFrame(data)
        banksName = str(bank['names'])
        data['bank_name'] = bank['names']
        data['bank_country'] = bank['country']
        # print(banksName)
        banksName =banksName.replace(' ','_')
        banksName = banksName.replace('/','_')
        data.to_latex('./reports/'+banksName+'.tex',encoding='utf-8')
