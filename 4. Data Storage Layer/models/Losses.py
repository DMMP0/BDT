class Losses:
    # TODO: add class description
    def __init__(self):
        self._fiscal_code = ""
        self._actual_debit_credit_cards = 0.00
        self._amount_due_mortgage = 0.00

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

    def get_actual_debit_credit_cards(self) -> float:
        return self._actual_debit_credit_cards

    def set_actual_debit_credit_cards(self, actual_debit_credit_cards: float):
        """ Sets value to 0 if the provided one is < 0"""
        if actual_debit_credit_cards < 0:
            self._actual_debit_credit_cards = 0
            print("Value was set to 0")
            return

        self._actual_debit_credit_cards = actual_debit_credit_cards

    def get_amount_due_mortgage(self) -> float:
        return self._amount_due_mortgage

    def set_amount_due_mortgage(self, amount_due_mortgage: float):
        """ Sets value to 0 if the provided one is < 0"""
        if amount_due_mortgage < 0:
            self._amount_due_mortgage = 0
            print("Value was set to 0")
            return

        self._amount_due_mortgage = amount_due_mortgage

