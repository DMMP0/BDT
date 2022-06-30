from dataclasses import dataclass


# import super

@dataclass
class Statement(object):
    """Class for storing the arriving messages from cloud storage"""
    purpose: str
    registeration_number: str
    company_name:str
    established_date: str
    country: str
    number_of_employes: int
    amount_of_credit:float
    purpose:str
    duration_in_months:int

    def __init__(self, data_dict):
        self.registeration_number = data_dict[1]
        self.amount_of_credit = data_dict[2]
        self.purpose = data_dict[3]
        self.duration_in_months = data_dict[4]