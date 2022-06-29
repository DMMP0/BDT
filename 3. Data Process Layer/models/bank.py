# Ex data
# {"Id_Number": "90a4aafd-d331-44f8-83d7-763f162d0507", "first_name": "wyndee", "last_name": "chawla", "sex": "Male",
# "DOB": "5/24/1981", "ethnicity": "native american", "education": "primary school", "phone_number": "191-038-9613",
# "email": "wyndee_chawla@gmail.com", "bank_name": "Volkswagen Bank", "bank_country": "Greece",
# "open_new_credit_in_6_months": 8, "ammount_in_6_months": "$44,097,908,334.00", "new_credit_in_12_months": 3.0,
# "new_credit_in_18_months": 2.0, "ammount_in_12_months": "$41,306.00", "ammount_in_18_months": "$66,146,588,994.00",
# "house_mortage": false, "amount_of_house_mortage": "0.0", "amount_duee_mortage": "0.0", "house_property": "$338,324.00",
# "total_house_amount": "0.0", "credit_card_number": 3, "credit_card_limit_total": 373288, "actual_debit_credit_cards": 2.0,
# "monthly_income": "$54,514.00", "savings": "$36,928.00", "other_savings": "$40,055.00"}
import os
import sys

sys.path.append(os.path.abspath(__file__))  # finds the parent directory
from .utils import get_meaning, clean_string, bank_synonyms, clean_money


# import re

class Bank:
    """Class for storing the arriving messages from cloud storage"""

    def __init__(self, d: dict):
        self.fiscal_code = ''
        self.bank_name = ''
        self.bank_country = ''
        self.amount_in_6_months = ''
        self.amount_in_12_months = ''
        self.amount_in_18_months = ''
        self.amount_of_house_mortgage = ''
        self.total_house_amount = ''
        self.credit_card_number = ''
        self.amount_due_mortgage = ''
        self.house_property = ''
        self.credit_card_limit_total = ''
        self.monthly_income = ''
        self.actual_debit_credit_cards = ''
        self.savings = ''
        self.other_savings = ''

        keys = list(d.keys())
        for key in keys:
            value = d[key]
            key = clean_string(key)  # lower and transform space to _
            meaning = get_meaning(key, bank_synonyms)
            if meaning == "fiscal_code":
                self.fiscal_code = str(value)
            elif meaning == "bank_name":
                self.bank_name = str(value)
            elif meaning == "bank_country":
                self.bank_country = str(value)
            elif meaning == "amount_in_6_months":
                self.amount_in_6_months = str(value)
            elif meaning == "amount_in_12_months":
                self.amount_in_12_months = str(value)
            elif meaning == "amount_in_18_months":
                self.amount_in_18_months = str(value)
            elif meaning == "amount_of_house_mortgage":
                self.amount_of_house_mortgage = str(value)
            elif meaning == "total_house_amount":
                self.total_house_amount = str(value)
            elif meaning == "credit_card_number":
                self.credit_card_number = str(value)
            elif meaning == "amount_due_mortgage":
                self.amount_due_mortgage = str(value)
            elif meaning == "house_property":
                self.house_property = str(value)
            elif meaning == "credit_card_limit_total":
                self.credit_card_limit_total = str(value)
            elif meaning == "actual_debit_credit_cards":
                self.actual_debit_credit_cards = str(value)
            elif meaning == "savings":
                self.savings = str(value)
            elif meaning == "other_savings":
                self.other_savings = str(value)
            elif meaning == "monthly_income":
                self.monthly_income = str(value)
            else:
                pass

    def make_sense(self):
        """@:returns a tuple of dictionaries: new_credit, credit_mix, assets, losses, bank"""
        new_credit = dict()
        credit_mix = dict()
        assets = dict()
        losses = dict()
        bank = dict()

        #
        new_credit['fiscal_code'] = self.fiscal_code
        new_credit["amount_in_12_months"] = clean_money(self.amount_in_12_months)
        new_credit['amount_in_6_months'] = clean_money(self.amount_in_6_months)
        new_credit['amount_in_18_months'] = clean_money(self.amount_in_18_months)

        credit_mix['fiscal_code'] = self.fiscal_code
        credit_mix['house_mortgage'] = clean_money(self.amount_of_house_mortgage)
        credit_mix['credit_card_number'] = self.credit_card_number.split(sep='.')[0]

        assets['fiscal_code'] = self.fiscal_code
        assets['total_house_amount'] = clean_money(self.total_house_amount)
        assets['monthly_income'] = clean_money(self.monthly_income)
        assets['savings'] = clean_money(self.savings)
        assets['other_savings'] = clean_money(self.other_savings)

        losses['fiscal_code'] = self.fiscal_code
        losses['actual_debit_credit_cards'] = self.actual_debit_credit_cards.split(sep='.')[0]
        losses['amount_due_mortgage'] = clean_money(self.amount_due_mortgage)

        bank['bank_name'] = self.bank_name
        bank['bank_country'] = self.bank_country
        bank['fiscal_code'] = self.fiscal_code

        return new_credit, credit_mix, assets, losses
