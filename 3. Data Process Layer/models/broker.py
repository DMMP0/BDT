import os
import sys

sys.path.append(os.path.abspath(__file__))  # finds the parent directory
from .utils import clean_string, clean_money, get_meaning, broker_synonyms

#{"agency_country": "Czech Republic",
# "agency_name": "CTC", "from30to60": 0, "from60to90": 0, "morethan90": 3
# "insolvent_ammount": "$13,884,270,465.00"}

class Broker:
    

    def __init__(self, d: dict):
        self.agency_country = ''
        self.agency_name = ''
        self.from60to90 = ''
        self.from30to60 = ''
        self.morethan90 = ''
        # self.debit_id = ''
        self.insolvent_amount = ''
        self.fiscal_code = ''
        keys = list(d.keys())
        for key in keys:
            value = d[key]
            key = clean_string(key)  # lower and transform space to _
            meaning = get_meaning(key, broker_synonyms)
            if meaning == "fiscal_code":
                self.fiscal_code = str(value)
            elif meaning == "agency_name":
                self.agency_name = str(value)
            elif meaning == "from60to90":
                self.from60to90 = str(value)
            # elif meaning == "debit_id":
            #     self.debit_id= str(value)
            elif meaning == "from30to60":
                self.from30to60= str(value)
            elif meaning == "morethan90":
                self.morethan90 = str(value)
            elif meaning == "insolvent_amount":
                self.insolvent_amount = str(value)
            else:
                pass

    def make_sense(self):
        """@:returns a dictionary: broker"""
        broker = dict()

        broker['fiscal_code'] = self.fiscal_code
        broker['agency_name'] = self.agency_name
        broker['from30to60'] = self.from30to60.split(sep='.')[0]
        broker['from60to90'] = self.from60to90.split(sep='.')[0]
        broker['morethan90'] = self.morethan90.split(sep='.')[0]
        broker['insolvent_amount'] = clean_money(self.insolvent_amount)

        return broker