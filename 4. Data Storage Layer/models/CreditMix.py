class CreditMix:
    # TODO: add class description
    def __init__(self):
        self._fiscal_code = ""
        self._installment_loan = False
        self._house_mortgage = False
        self._credit_cards_number = 0

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

    def get_installment_loan(self) -> bool:
        return self._installment_loan
    
    def set_installment_loan(self, installment_loan: bool):
        self._installment_loan = installment_loan

    def get_house_mortgage(self) -> bool:
        return self._house_mortgage

    def set_house_mortgage(self, house_mortgage: bool):
        self._house_mortgage = house_mortgage

    def get_credit_cards_number(self) -> int:
        return self._credit_cards_number

    def set_credit_cards_number(self, n: int):
        if n < 0:
            self._credit_cards_number = 0
            print("Value was < 0, so it was set to 0")
            return
        self._credit_cards_number = n
        