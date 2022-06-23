class Assets:
    # Todo: add class description

    def __init__(self):
        self._fiscal_code = ""
        self._total_house_amount = 0.00
        self._monthly_income = 0.00
        self._savings = 0.00
        self._other_savings = 0.00

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

    def get_total_house_amount(self) -> float:
        return self._total_house_amount

    def set_total_house_amount(self, total_house_amount: float):
        """ Sets value to 0 if the provided one is < 0"""
        if total_house_amount < 0:
            self._total_house_amount = 0
            print("Value was less than 0, so it has been converted to 0")
            return 
        
        self._total_house_amount = total_house_amount

    def get_monthly_income(self) -> float:
        return self._monthly_income

    def set_monthly_income(self, monthly_income: float):
        """ Sets value to 0 if the provided one is < 0"""
        if monthly_income < 0:
            self._monthly_income = 0
            print("Value was less than 0, so it has been converted to 0")
            return

        self._monthly_income = monthly_income

    def get_savings(self) -> float:
        return self._savings

    def set_savings(self, savings: float):
        """ Sets value to 0 if the provided one is < 0"""
        if savings < 0:
            self._savings = 0
            print("Value was less than 0, so it has been converted to 0")
            return

        self._savings = savings

    def get_other_savings(self) -> float:
        return self._other_savings

    def set_other_savings(self, other_savings: float):
        """ Sets value to 0 if the provided one is < 0"""
        if other_savings < 0:
            self._other_savings = 0
            print("Value was less than 0, so it has been converted to 0")
            return

        self._other_savings = other_savings
            