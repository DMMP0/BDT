from dataclasses import dataclass


@dataclass
class Bank:
    """Class for storing the arriving messages from cloud storage"""

    # fiscal_code: str
    # bank_name: str
    # bank_country: str
    # open_new_credit_in_6_months: int
    # amount_in_6_months : float
    # amount_in_12_months: float
    # new_credit_in_12_months:int
    # amount_in_18_months: float
    # new_credit_in_18_months : int
    # house_mortgage : bool
    # amount_of_house_mortgage : float
    # amount_due_mortgage :float
    # house_property : bool
    # total_house_amount : float
    # credit_card_number :  int
    # credit_card_limit_total : float
    # actual_debit_credit_cards : int
    # monthly_income = float
    # savings : float
    # savings : float
    
    fiscal_code: str
    bank_name: str
    bank_country: str
    open_new_credit_in_6_months: str
    amount_in_6_months : str
    amount_in_12_months: str
    new_credit_in_12_months:str
    amount_in_18_months: str
    new_credit_in_18_months : str
    house_mortgage : str
    amount_of_house_mortgage : str
    amount_due_mortgage :str
    house_property : str
    total_house_amount : str
    credit_card_number :  str
    credit_card_limit_total : str
    actual_debit_credit_cards : str
    monthly_income = str
    savings : str
    savings : str


    def __init__(self,bank_data):
            self.fiscal_code = bank_data.get('Id_Number')
            self.email = bank_data.get('email')
            self.bank_name = bank_data.get('bank_name')
            self.bank_country = bank_data.get('bank_country')
            self.open_new_credit_in_6_months = bank_data.get('open_new_credit_in_6_months')
            self.amount_in_6_months = bank_data.get('amount_in_6_months')
            self.amount_in_12_months = bank_data.get('amount_in_12_months')
            self.new_credit_in_12_months = bank_data.get('new_credit_in_12_months')
            self.amount_in_18_months = bank_data.get('amount_in_18_months')
            self.new_credit_in_18_months = bank_data.get('new_credit_in_18_months')
            self.house_mortgage = bank_data.get('house_mortgage')
            self.amount_of_house_mortgage = bank_data.get('amount_of_house_mortgage')
            self.amount_due_mortgage = bank_data.get('amount_due_mortgage')
            self.house_property = bank_data.get('house_property')
            self.total_house_amount = bank_data.get('total_house_amount')
            self.credit_card_number = bank_data.get('credit_card_number')
            self.credit_card_limit_total = bank_data.get('credit_card_limit_total')
            self.actual_debit_credit_cards = bank_data.get('actual_debit_credit_cards')
            self.monthly_income = bank_data.get('monthly_income')
            self.savings = bank_data.get('savings')
            self.savings = bank_data.get('other_savings')