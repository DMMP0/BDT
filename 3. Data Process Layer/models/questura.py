from dataclasses import dataclass

@dataclass
class Questura:
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