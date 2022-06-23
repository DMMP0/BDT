class Firm:
    """A class representing a firm (corporation)"""
    
    def __init__(self):
        self._registration_number = ""
        self._name = "Dummy corporation"
        self._establishment_date = ""
        self._employees = 0
        self._country = ""
        
    def get_registration_number(self) -> str:
        return self._registration_number
    
    def set_registration_number(self, registration_number: str):
        self._registration_number = registration_number

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str):
        self._name = name

    def get_establishment_date(self) -> str:
        return self._establishment_date

    def set_establishment_date(self, establishment_date: str):
        self._establishment_date = establishment_date

    def get_country(self) -> str:
        return self._country

    def set_country(self, country: str):
        self._country = country
        
    def get_employees(self) -> int:
        return self._employees

    def set_employees(self, n: int):
        if n < 0:
            self._employees = 0
            print("Value was < 0, so it was set to 0")
            return
        self._employees = n