class CreditHistory:
    # TODO: add class description
    def __init__(self):
        self._fiscal_code = ""
        self._from30to60 = 0	
        self._from60to90 = 0	
        self._more_than90 = 0
        self._insolvent_amount = 0.00

    # getters and setters
    def get_fiscal_code(self) -> str:
        return self._fiscal_code

    def set_fiscal_code(self, fiscal_code: str):
        # checks
        if fiscal_code == "":
            print("Couldn't modify fiscal code, string was empty")
            return
        # fiscal code is not generated correctly, so the checks will not be implemented

        self._fiscal_code = fiscal_code
        
    def get_from_30_to_60(self) -> int:
        return self._from30to60
    
    def set_from_30_to_60(self, f30to60):
        if f30to60 <= 0:
            self._from30to60 = 0
            print("Value was less than 0, so it has been set to to 0")
            return 
        
        self._from30to60 = f30to60

    def get_from_60_to_90(self) -> int:
        return self._from60to90

    def set_from_60_to_90(self, f60to90):
        if f60to90 <= 0:
            self._from60to90 = 0
            print("Value was less than 0, so it has been set to to 0")
            return

        self._from60to90 = f60to90

    def get_more_than90(self) -> int:
        return self._more_than90

    def set_more_than90(self, m90):
        if m90 <= 0:
            self._more_than90 = 0
            print("Value was less than 0, so it has been set to to 0")
            return

        self._more_than90 = m90
    
    def get_insolvent_amount(self) -> float:
        return self._insolvent_amount

    def set_insolvent_amount(self, insolvent_amount: float):
        """ Sets value to 0 if the provided one is < 0"""
        if insolvent_amount < 0:
            self._insolvent_amount = 0
            print("Value was set to 0")
            return

        self._insolvent_amount = insolvent_amount
        
    