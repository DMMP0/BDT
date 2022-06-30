from dataclasses import dataclass


@dataclass
class Bank:
    """Class for storing the arriving messages from cloud storage"""
    
    
    amount_in_12_months: float
    house_mortgage : float
    amount_due_mortgage :float
    total_house_amount : float
    credit_card_number :  int
    actual_debit_credit_cards : float
    monthly_income = float
    savings : float
    other_savings : float


    def __init__(self,credit_mix,assets,losses,new_credit):
            self.amount_in_12_months = new_credit[0]
            self.house_mortgage = credit_mix[0]
            self.amount_due_mortgage = losses[1]
            self.total_house_amount = assets[0]
            self.credit_card_number = credit_mix[1]
            self.actual_debit_credit_cards = losses[0]
            self.monthly_income = assets[1]
            self.savings = assets[2]
            self.other_savings = assets[3]