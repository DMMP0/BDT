class CreditData:
    # TODO: add description

    def __init__(self):
        self._firm_registration_number = ""
        self._amount_of_credit = 0.00
        self._purpose = ""
        self._duration_in_months = 0

    def get_firm_registration_number(self) -> str:
        return  self._firm_registration_number
    
    def set_firm_registration_number(self, firm_registration_number: str):
        self._firm_registration_number = firm_registration_number

    def get_purpose(self) -> str:
        return self._purpose

    def set_purpose(self, purpose: str):
        self._purpose = purpose
        
    def get_duration_in_months(self) -> int:
        return self._duration_in_months

    def set_duration_in_months(self, n: int):
        if n < 0:
            self._duration_in_months = 0
            print("Value was < 0, so it was set to 0")
            return
        self._duration_in_months = n
        
    def get_amount_of_credit(self) -> float:
        return self._amount_of_credit

    def set_amount_of_credit(self, n: float):
        if n < 0:
            self._amount_of_credit = 0
            print("Value was < 0, so it was set to 0")
            return
        self._amount_of_credit = n
