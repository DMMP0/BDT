from dataclasses import dataclass

from cv2 import Stitcher_ERR_CAMERA_PARAMS_ADJUST_FAIL
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
        self.purpose= data_dict.get('purpose')
        self.registeration_number= data_dict.get('registeration_number')
        self.company_name= data_dict.get('company_name')
        self.established_date= data_dict.get('establied_date')
        self.country= data_dict.get('country')
        self.number_of_employes = data_dict.get('number_of_employes')
        self.amount_of_credit = data_dict.get('amount_of_credit')
        self.purpose = data_dict.get('purpose')
        self.duration_in_months = data_dict.get('duration_in_months')


