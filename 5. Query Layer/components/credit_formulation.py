
import set_bank_data as bank
import set_broker_data as broker
import set_questura_data as questura
import set_firm_data as f
import set_person_data as p
import sys,os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # finds the current directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the parent directory
from models.bank import Bank
from models.broker import Broker
from models.questura import Questura
from models.statement import Statement
from models.firm import Firm
from models.person_info import Person


key = '13a9cd05-07ba-4d47-8a46-1cfa22b045a6'

def credit_score_formulation(firm_data:Firm,credit_data:Statement,credit_history:Broker,bank_data:Bank,questura_data:Questura):
        print()
        
        print(credit_history.insolvent_ammount)
        print(questura_data.bankruptcy)
        print(bank_data.total_house_amount)
        print(bank_data.monthly_income)
        print(bank_data.savings)
        print(bank_data.other_savings)
        print(bank_data.actual_debit_credit_cards)
        print(bank_data.amount_due_mortgage)
        FISCO = 240

        if bank_data.house_mortgage != 0.0 :
            FISCO += 30
        FISCO += 8*(bank_data.credit_card_number)
        FISCO -= (bank_data.amount_in_12_months/190)

        print(FISCO)
        if questura_data.bankruptcy == 0:
            FISCO +=160
        if questura_data.bankruptcy == 1:
            FISCO +=100
        if questura_data.bankruptcy == 2:
            FISCO +=0


        print("FISCO",FISCO)
        FISCO -= (credit_history.insolvent_ammount/ 0.83333)
        print("FISCO",FISCO)
        # print(type( bank_data.total_house_amount))
        # print(type( bank_data.monthly_income))
        # print(type( bank_data.savings))
        # print(type( bank_data.other_savings))
        # print(type( float(bank_data.actual_debit_credit_cards)))
        # print(type(float(bank_data.amount_due_mortgage)))

        raw_range = bank_data.total_house_amount+ 12*(float(bank_data.monthly_income)) + 0.8*(bank_data.savings) + 0.5*(bank_data.other_savings) - 5.0*(float(bank_data.actual_debit_credit_cards)) - bank_data.amount_due_mortgage
        linear_trans = (raw_range+600)*0.000196

        print("FISCO",FISCO)
        FISCO += linear_trans
        print("FISCO",FISCO)
        if(FISCO < 0):
            FISCO = 0
        if(FISCO > 700):
            FISCO = 700

        print("Your score is",FISCO)


def call_data_all(key):
    ## getting personal data
    personal_data = p.read_data(key)
    person = Person(personal_data[0])
    firm_id = person.firm_registeration_number
    print(firm_id)

    ## getting firm and credit data
    (firm_data,credit_data) = f.read_data(firm_id)
    firm_data = Firm(firm_data[0])
    credit_data = Statement(credit_data[0])

    ## getting credit_history
    credit_history = broker.read_data(key)
    credit_history = Broker(credit_history[0])
    print(credit_history.insolvent_ammount)

    ## getting bank data 
    (credit_mix,assets,losses,new_credit) = bank.read_data(key)
    bank_data = Bank(credit_mix[0],assets[0],losses[0],new_credit[0])
    print(bank_data.amount_in_12_months)

    ## getting questura data 
    (bankruptcy) = questura.read_data(key)
    questura_data = Questura(bankruptcy)
    print(questura_data.bankruptcy)

    ## now calculate the values
    credit_score_formulation(firm_data,credit_data,credit_history,bank_data,questura_data)



call_data_all(key)    