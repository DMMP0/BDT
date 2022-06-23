class NewCredit:
    # TODO: add class description
    def __init__(self):
        self._fiscal_code = ""
        self._amount_in_12_months = 0.00

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

    def get_amount_in_12_monthss(self) -> float:
        return self._amount_in_12_months

    def set_amount_in_12_months(self, amount_in_12_months: float):
        """ Sets value to 0 if the provided one is < 0"""
        if amount_in_12_months < 0:
            self._amount_in_12_months = 0
            print("Value was set to 0")
            return

        self._amount_in_12_months = amount_in_12_months



