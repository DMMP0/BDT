### Example of statement:
### {"Unnamed: 0": 36538, "Id_Number": "0b6c2e52-b9aa-4b77-966f-b4ed712c0c88", "first_name": "zafeiroula", "last_name": "camburn", "sex": "Female", "DOB": "4/13/1980",
# "ethnicity": "caribbean", "education": "middle school", "phone_number": "658-667-6356", "email": "headquarters@canadalifefinancialcorp.org", "purpose": "employee",
# "registeration_number": "c5bca43a-6b71-4e5f-8861-7d4ddf5d547e", "company_name": "Canada Life Financial Corp.", "establied_date": "12/7/1995", "country": "Canada", "number_of_employes": 20}




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
    questura_country: str
    bankruptcy: str
    inscred: str
    fraudis: str
    investigation: str
    accused: str
    condamned: str
    civ_pass: str

    def __init__(self, d:dict):
