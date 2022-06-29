from services.send_firm_data import main as firm_main
from services.send_bank_data import main as bank_main
from services.send_broker_data import main as broker_main
from services.send_personal_data import main as personal_main

from services.send_questura_data import main as questura_main
import redis

r = redis.StrictRedis()
while True:
    firm_main(r)
    print("Firm data sent")
    personal_main(r)
    print("personal data sent")
    bank_main(r)
    print("bank data sent")
    broker_main(r)
    print("broker data sent")
    questura_main(r)
    print("questura data sent")

