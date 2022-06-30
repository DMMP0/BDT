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
        self.fiscal_code = data_dict[1]
        self.first_name= data_dict[2]
        self.last_name= data_dict[3]
        self.sex= data_dict[4]
        self.DOB= data_dict[5]
        self.ethnicity= data_dict[6]
        self.education= data_dict[7]
        self.email= data_dict[9]
        self.phone_number= data_dict[10]
        self.state= data_dict[11]
        self.firm_registeration_number= data_dict[12]
        
