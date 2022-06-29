from dataclasses import dataclass

@dataclass
class Questura:
    """Class for storing the arriving messages from cloud storage"""

    fiscal_code: str
    questura_country: str
    bankruptcy: bool
    inscred: float
    fraudis: bool
    investigation: bool
    accused: bool
    condamned: bool
    civ_pass: bool

    def __init__(self,bank_data):
            self.fiscal_code = bank_data.get('Id_Number')
            self.questura_country = bank_data.get('questura_country')
            self.bankruptcy = bank_data.get('bankruptcy')
            self.inscred = bank_data.get('inscred')
            self.fraudis = bank_data.get('fraudis')
            self.investigation = bank_data.get('investegation')
            self.accused = bank_data.get('accused')
            self.condamned = bank_data.get('condamned')
            self.civ_pass = bank_data.get('civ_pass')
