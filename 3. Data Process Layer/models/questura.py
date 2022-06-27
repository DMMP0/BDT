import os
import sys

sys.path.append(os.path.abspath(__file__))  # finds the parent directory
from .utils import get_meaning, clean_string, questura_synonyms, decode_t_f


# {"Unnamed: 0": 118851, "Id_Number": "636932be-b794-40b2-ba36-eb64baca449a", "first_name": "lucresha",
# "last_name": "karratti", "sex": "Male", "DOB": "8/17/1971", "ethnicity": "caribbean", "education": "bachelor",
# "phone_number": "158-466-4985", "email": "lucresha_karratti@gmail.com", "questura_country": "United Kingdom",
# "bankruptcy": true, "inscred": "$725,658.00", "fraudis": true, "investegation": false, "accused": true,
# "condamned": false, "civ_pass": false}


class Questura:
    """Class for storing the arriving messages from cloud storage"""


    def __init__(self, d: dict):
        self.fiscal_code = ''
        self.questura_country = ''
        self.bankruptcy = ''
        self.inscred = ''
        self.fraudis = ''
        self.investigation = ''
        self.accused = ''
        self.condamned = ''
        self.civ_pass = ''
        keys = list(d.keys())
        for key in keys:
            value = d[key]
            key = clean_string(key)  # lower and transform space to _
            meaning = get_meaning(key, questura_synonyms)
            if meaning == "fiscal_code":
                self.fiscal_code = str(value)
            elif meaning == "questura_country":
                self.questura_country =str(value)
            elif meaning == "bankruptcy":
                self.bankruptcy = str(value)
            # elif meaning == "inscred":
            #     self.inscred = value
            elif meaning == "fraudis":
                self.fraudis = str(value)
            elif meaning == "investigation":
                self.investigation =str(value)
            elif meaning == "accused":
                self.accused = str(value)
            elif meaning == "condamned":
                self.condamned = str(value)
            elif meaning == "civ_pass":
                self.civ_pass = str(value)
            else:
                pass

    def make_sense(self):
        """@:returns a dictionary: criminal_records"""
        criminal_records = dict()

        criminal_records['fiscal_code'] = self.fiscal_code
        if clean_string(self.bankruptcy) == 'true':
            if clean_string(self.fraudis) == 'true':
                criminal_records['bankruptcy'] = '2'
            else:
                criminal_records['bankruptcy'] = 1
        else:
            criminal_records['bankruptcy'] = 0
        criminal_records['questura_country'] = self.questura_country
        # we encoded true and false as bits
        criminal_records['investigation'] = decode_t_f(self.investigation)
        criminal_records['accused'] = decode_t_f(self.accused)
        criminal_records['condamned'] = decode_t_f(self.condamned)
        criminal_records['civ_pass'] = decode_t_f(self.civ_pass)

        return criminal_records
