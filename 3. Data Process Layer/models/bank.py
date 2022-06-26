#Ex data
# {"Id_Number": "90a4aafd-d331-44f8-83d7-763f162d0507", "first_name": "wyndee", "last_name": "chawla", "sex": "Male",
# "DOB": "5/24/1981", "ethnicity": "native american", "education": "primary school", "phone_number": "191-038-9613",
# "email": "wyndee_chawla@gmail.com", "bank_name": "Volkswagen Bank", "bank_country": "Greece",
# "open_new_credit_in_6_months": 8, "ammount_in_6_months": "$44,097,908,334.00", "new_credit_in_12_months": 3.0,
# "new_credit_in_18_months": 2.0, "ammount_in_12_months": "$41,306.00", "ammount_in_18_months": "$66,146,588,994.00",
# "house_mortage": false, "amount_of_house_mortage": "0.0", "amount_duee_mortage": "0.0", "house_property": "$338,324.00",
# "total_house_amount": "0.0", "credit_card_number": 3, "credit_card_limit_total": 373288, "actual_debit_credit_cards": 2.0,
# "monthly_income": "$54,514.00", "savings": "$36,928.00", "other_savings": "$40,055.00"}

from utils import get_meaning, clean_string, bank_synonyms
# import re

class Bank:
    """Class for storing the arriving messages from cloud storage"""

    fiscal_code: str
    bank_name: str
    bank_country: str
    amount_in_6_months: str
    amount_in_12_months: str
    amount_in_18_months: str
    amount_of_house_mortgage: str
    total_house_amount: str
    credit_card_number: str
    amount_due_mortgage: str
    house_property: str
    credit_card_limit_total: str
    monthly_income: str
    actual_debit_credit_cards: str
    savings: str
    other_savings: str

    def __init__(self, d: dict):
        keys = list(d.keys())
        for key in keys:
            value = d[key]
            key = clean_string(key)  # lower and transform space to _
            meaning = get_meaning(key, bank_synonyms)
            if meaning == "fiscal_code":
                self.fiscal_code = value
            elif meaning == "bank_name":
                self.bank_name = value
            elif meaning == "bank_country":
                self.bank_country = value
            elif meaning == "amount_in_6_months":
                self.amount_in_6_months = value
            elif meaning == "amount_in_12_months":
                self.amount_in_12_months = value
            elif meaning == "amount_in_18_months":
                self.amount_in_18_months = value
            elif meaning == "amount_of_house_mortgage":
                self.amount_of_house_mortgage = value
            elif meaning == "total_house_amount":
                self.total_house_amount = value
            elif meaning == "credit_card_number":
                self.credit_card_number = value
            elif meaning == "amount_due_mortgage":
                self.amount_due_mortgage = value
            elif meaning == "house_property":
                self.house_property = value
            elif meaning == "credit_card_limit_total":
                self.credit_card_limit_total = value
            elif meaning == "actual_debit_credit_cards":
                self.actual_debit_credit_cards = value
            elif meaning == "savings":
                self.savings = value
            elif meaning == "other_savings":
                self.other_savings = value
            else:
                pass

    def make_sense(self):
        """@:returns a tuple of dictionaries, for the records of personal data and firm"""
        new_credit = dict()
        credit_mix = dict()
        assets = dict()
        losses = dict()

        #
        new_credit['fiscal_code'] = self.fiscal_code
        new_credit["amount_in_12_months"] = self.amount_in_12_months.replace(",",'').replace('$','')  # I know, I know, should be done with regex
        new_credit['amount_in_6_months'] = self.amount_in_6_months.replace(",",'').replace('$','')
        new_credit['amount_in_18_months'] = self.amount_in_18_months.replace(",",'').replace('$','')

        credit_mix['fiscal_code'] = self.fiscal_code
        credit_mix['house_mortgage'] = self.amount_of_house_mortgage.replace(",",'').replace('$','')
        credit_mix['credit_card_number'] = self.credit_card_number.split(sep='.')[0]
        if self.sex == "male":
            personal_data["sex"] = "1"
        elif self.sex == "female":
            personal_data['sex'] = "0"
        else:
            personal_data['sex'] = '2'
        personal_data['DOB'] = self.DOB
        personal_data['ethnicity'] = self.ethnicity
        personal_data['highest_degree'] = self.education
        personal_data['email'] = self.email
        personal_data['address'] = " "
        personal_data['phone_number'] = self.phone_number
        personal_data['state'] = self.country
        personal_data['firm_registration'] = self.registration_number

        firm['registeration_number'] = self.registration_number
        firm['company_name'] = self.company_name
        firm['established_date'] = self.established_date
        firm['number_of_employes'] = self.employees
        firm['country'] = self.country

        return personal_data, firm