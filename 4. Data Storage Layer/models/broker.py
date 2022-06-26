
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
    insolvent_ammount:str



    def __init__(self,bank_data):
            self.fiscal_code = bank_data.get('Id_Number')
            self.agency_country = bank_data.get('agency_country')
            self.agency_name = bank_data.get('agency_name')
            self.from60to90 = bank_data.get('from60to90')
            self.from30to60 = bank_data.get('from30to60')
            self.morethan90 = bank_data.get('morethan90')
            self.debit_id = bank_data.get('debit_id')
            self.insolvent = bank_data.get('insolvent')
            self.insolvent_ammount = bank_data.get('insolvent_ammount')