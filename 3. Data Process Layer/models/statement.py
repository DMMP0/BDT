### Example of statement:
### {"Unnamed: 0": 36538, "Id_Number": "0b6c2e52-b9aa-4b77-966f-b4ed712c0c88", "first_name": "zafeiroula", "last_name": "camburn", "sex": "Female", "DOB": "4/13/1980",
# "ethnicity": "caribbean", "education": "middle school", "phone_number": "658-667-6356", "email": "headquarters@canadalifefinancialcorp.org", "purpose": "employee",
# "registeration_number": "c5bca43a-6b71-4e5f-8861-7d4ddf5d547e", "company_name": "Canada Life Financial Corp.", "establied_date": "12/7/1995", "country": "Canada", "number_of_employes": 20}

from utils import clean_string, statement_synonyms, get_meaning


class Statement:
    """Class for storing the arriving messages from cloud storage"""

    fiscal_code: str
    first_name: str
    last_name: str
    sex: str
    DOB: str
    ethnicity: str
    education: str
    phone_number: str
    email: str
    purpose: str
    firm_id: str
    company_name: str
    established_date: str
    country: str
    employees: str

    def __init__(self, d: dict):
        keys = list(d.keys())
        for key in keys:
            value = d[key]
            key = clean_string(key)  # lower and transform space to _
            meaning = get_meaning(key, statement_synonyms)
            if meaning == "fiscal_code":
                self.fiscal_code = value
            elif meaning == "first_name":
                self.first_name = value
            elif meaning == "last_name":
                self.last_name = value
            elif meaning == "DOB":
                self.DOB = value
            elif meaning == "ethnicity":
                self.ethnicity = value
            elif meaning == "education":
                self.education = value
            elif meaning == "phone_number":
                self.phone_number = value
            elif meaning == "email":
                self.email = value
            elif meaning == "purpose":
                self.purpose = value
            elif meaning == "registration_number":
                self.registration_number = value
            elif meaning == "company_name":
                self.company_name = value
            elif meaning == "established_date":
                self.established_date = value
            elif meaning == "country":
                self.country = value
            elif meaning == "employees":
                self.employees = value
            # else
            #   pass

    def make_sense(self):
        """@:returns a tuple of dictionaries, for the records of personal data and firm"""
        personal_data = dict()
        firm = dict()

        # personal data
        personal_data["fiscal_code"] = self.fiscal_code
        personal_data['first_name'] = self.first_name
        personal_data['last_name'] = self.last_name
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



