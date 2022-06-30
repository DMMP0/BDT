import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # finds the current directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the parent directory

import components.set_bank_data as bank
import components.set_broker_data as broker
import components.set_questura_data as questura
import components.set_firm_data as f
import components.set_person_data as p



from models.bank import Bank
from models.broker import Broker
from models.questura import Questura
from models.statement import Statement
from models.firm import Firm
from models.person_info import Person


key = '5dd541fd-0f36-4b36-92b4-b29a22ef2acc'

def credit_score_formulation(firm_data:Firm,credit_data:Statement,credit_history:Broker,bank_data:Bank,questura_data:Questura):  
        # print(credit_history.insolvent_ammount) ## pick the highest
        # print(questura_data.bankruptcy)
        # print(bank_data.total_house_amount)
        # print(bank_data.monthly_income)
        # print(bank_data.savings)
        # print(bank_data.other_savings)
        # print(bank_data.actual_debit_credit_cards)
        # print(bank_data.amount_due_mortgage)
        # print(bank_data.amount_due_mortgage)
        data_used = []
        
        if(bank_data.house_mortgage == None and credit_history.insolvent_ammount == None and questura_data.bankruptcy == None and bank_data.monthly_income == None):
            print("The complete data was not found we need some time to process your information")
            return False
        else:
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
            FISCO -= (credit_history.insolvent_ammount/ 83333)
            print("FISCO",FISCO)
            # print(type( bank_data.total_house_amount))
            # print(type( bank_data.monthly_income))
            print("savings",bank_data.savings)
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
            data_used.append(credit_history.insolvent_ammount)
            data_used.append(questura_data.bankruptcy)
            data_used.append(bank_data.total_house_amount)
            data_used.append(bank_data.monthly_income)
            data_used.append(str(bank_data.savings))
            data_used.append(bank_data.other_savings)
            data_used.append(float(bank_data.actual_debit_credit_cards))
            data_used.append(bank_data.amount_due_mortgage)
            return (FISCO,data_used)


def call_data_all(key):
    
    tag = True
    ## getting personal data
    personal_data = p.read_data(key)
    person = Person(personal_data[0])
    firm_id = person.firm_registeration_number
    print(firm_id)
    ## getting firm and credit data
    (firm_data,credit_data) = f.read_data(firm_id)
    print("Credit data len",len(credit_data))
    if(len(credit_data) != 0 and len(firm_data) !=0):
        firm_data = Firm(firm_data[0])
        credit_data = Statement(credit_data[0])
    else:
        tag = False

    ## getting credit_history
    
    credit_history = broker.read_data(key)
    if(len(credit_history) != 0):
        credit_history = Broker(credit_history[0])
        print(credit_history.insolvent_ammount)
    else:
        tag = False

    ## getting bank data 
    (credit_mix,assets,losses,new_credit) = bank.read_data(key)
    if(len(credit_mix) != 0 and len(assets) != 0 and len(losses) != 0 and len(new_credit) != 0):
        bank_data = Bank(credit_mix[0],assets[0],losses[0],new_credit[0])
        print(bank_data.amount_in_12_months)
    else:
        tag = False

    ## getting questura data 
    (bankruptcy) = questura.read_data(key)
    if(len(bankruptcy) != 0):
        questura_data = Questura(bankruptcy)
        print(questura_data.bankruptcy)
    else:
        tag = False

    ## now calculate the values
    if(tag):
        (FISCO,data_used) = credit_score_formulation(firm_data,credit_data,credit_history,bank_data,questura_data)
        return (FISCO,data_used)
    else:
        print("No credit score calculated due to incomplete information")
        return ("No credit score calculated due to incomplete information",False)
  

call_data_all(key)