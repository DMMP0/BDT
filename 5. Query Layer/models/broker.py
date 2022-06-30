
from dataclasses import dataclass




@dataclass
class Broker:
    fiscal_code: str
    agency_country:str
    agency_name: str
    from60to90:str
    from30to60:str
    morethan90:str
    debit_id:int
    insolvent:bool
    insolvent_ammount:float



    def __init__(self,bank_data):
            self.insolvent_ammount = bank_data[0]