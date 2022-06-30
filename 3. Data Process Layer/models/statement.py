### Example of statement:
# {"Unnamed: 0": 123657, "Id_Number": "ffed21b1-04fd-429c-8b4c-44164697eb81", "first_name": "mendez-ortiz",
# "last_name": "fujino", "sex": "Male", "DOB": "4/16/1996", "ethnicity": "caribbean", "education": "phd",
# "phone_number": "687-828-7488", "Personal_email": "mendez-ortiz_fujino@gmail.com", "purpose": "validation",
# "registeration_number": "b700a831-9993-4446-aa49-b2d3f351122c", "company_name": "Mercury Scheduling Systems Inc.",
# "establied_date": "7/4/1979", "country": "Canada", "number_of_employes": 18, "email":
# "headquarters@mercuryschedulingsystemsinc.org", "amount_of_credit": "$32,173,793,107.00", "duration_in_months": 8}
import os
import sys

sys.path.append(os.path.abspath(__file__))  # finds the parent directory
from .utils import clean_string, statement_synonyms, get_meaning, clean_money


class Statement:
    """Class for storing the arriving messages from cloud storage"""

    def __init__(self, d: dict):
        self.fiscal_code = ''
        self.first_name = ''
        self.last_name = ''
        self.sex = ''
        self.DOB = ''
        self.ethnicity = ''
        self.education = ''
        self.phone_number = ''
        self.email = ''
        self.pemail = ''
        self.purpose = ''
        self.firm_id = ''
        self.company_name = ''
        self.established_date = ''
        self.country = ''
        self.employees = ''
        self.amount_of_credit = ''
        self.duration_in_months = ''
        keys = list(d.keys())
        for key in keys:
            value = d[key]
            key = clean_string(key)  # lower and transform space to _
            meaning = get_meaning(key, statement_synonyms)
            if meaning == "fiscal_code":
                self.fiscal_code = str(value)
            elif meaning == "first_name":
                self.first_name = str(value)
            elif meaning == "last_name":
                self.last_name = str(value)
            elif meaning == "DOB":
                self.DOB = str(value)
            elif meaning == "sex":
                self.sex = str(value)
            elif meaning == "ethnicity":
                self.ethnicity = str(value)
            elif meaning == "education":
                self.education = str(value)
            elif meaning == "phone_number":
                self.phone_number = str(value)
            elif meaning == "email":
                self.email = str(value)
            elif meaning == "purpose":
                self.purpose = str(value)
            elif meaning == "registration_number":
                self.registration_number = str(value)
            elif meaning == "company_name":
                self.company_name = str(value)
            elif meaning == "established_date":
                self.established_date = str(value)
            elif meaning == "country":
                self.country = str(value)
            elif meaning == "employees":
                self.employees = str(value)
            elif meaning == "amount_of_credit":
                self.amount_of_credit = str(value)
            elif meaning == "duration_in_months":
                self.duration_in_months = str(value)
            elif meaning == "pmail":
                self.pemail = str(value)
            else:
                pass

    def make_sense(self):
        """@:returns a tuple of dictionaries: personal data , firm, credit_data"""
        personal_data = dict()
        firm = dict()
        credit_data = dict()

        # personal data
        personal_data["fiscal_code"] = self.fiscal_code
        personal_data['first_name'] = self.first_name
        personal_data['last_name'] = self.last_name
        if clean_string(self.sex) == "male":
            personal_data["sex"] = "1"
        elif clean_string(self.sex) == "female":
            personal_data['sex'] = "0"
        else:
            personal_data['sex'] = '2'
        personal_data['DOB'] = self.DOB
        personal_data['ethnicity'] = self.ethnicity
        personal_data['highest_degree'] = self.education
        personal_data['email'] = self.pemail
        personal_data['address'] = " "
        personal_data['phone_number'] = self.phone_number
        personal_data['state'] = self.country
        personal_data['firm_registration'] = self.registration_number

        firm['registeration_number'] = self.registration_number
        firm['company_name'] = self.company_name
        firm['established_date'] = self.established_date
        firm['number_of_employes'] = self.employees
        firm['country'] = self.country
        firm['email'] = self.email

        credit_data['registeration_number'] = self.registration_number
        credit_data['amount_of_credit'] = clean_money(self.amount_of_credit)
        credit_data['purpose'] = self.purpose
        credit_data['duration_in_months'] = self.duration_in_months

        return personal_data, firm, credit_data
