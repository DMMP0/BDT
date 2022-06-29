from dataclasses import dataclass
import email
from sre_parse import State

from cv2 import Stitcher_ERR_CAMERA_PARAMS_ADJUST_FAIL
# import super

@dataclass
class Person(object):
    """Class for storing the arriving messages from cloud storage"""

    fiscal_code: str
    first_name: str
    last_name: str
    sex: str
    DOB: str
    country:str
    ethnicity: str
    education: str
    phone_number: str
    email : str
    firm_registeration_number:str
    state:str

    def __init__(self, data_dict):
        self.fiscal_code = data_dict.get('Id_Number')
        self.first_name= data_dict.get('first_name')
        self.last_name= data_dict.get('last_name')
        self.sex= data_dict.get('sex')
        self.DOB= data_dict.get('DOB')
        self.ethnicity= data_dict.get('ethnicity')
        self.education= data_dict.get('education')
        self.phone_number= data_dict.get('phone_number')
        self.email= data_dict.get('email')
        self.firm_registeration_number= data_dict.get('registeration_number')
        self.country= data_dict.get('country')
        self.state= data_dict.get('country')
