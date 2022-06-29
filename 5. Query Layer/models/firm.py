from dataclasses import dataclass

from cv2 import Stitcher_ERR_CAMERA_PARAMS_ADJUST_FAIL
# import super

@dataclass
class Firm(object):
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
        self.registeration_number= data_dict[1]
        self.company_name= data_dict[2]
        self.established_date= data_dict[3]
        self.number_of_employes = data_dict[4]
        self.country= data_dict[5]
        self.amount_of_credit = data_dict
        self.purpose = data_dict
        self.duration_in_months = data_dict


