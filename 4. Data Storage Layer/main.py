from services.send_firm_data import main as firm_main
from services.send_bank_data import main as bank_main
from services.send_broker_data import main as broker_main
from services.send_personal_data import main as personal_main

from services.send_questura_data import main as questura_main
import redis
import threading

r = redis.StrictRedis()
while True:
    #firm_main(r)
    print("Firm data sent")
    #personal_main(r)
    print("personal data sent")
    #t1 = threading.Thread(target=bank_main, args=(r,))
    #t2 = threading.Thread(target=broker_main, args=(r,))
    t3 = threading.Thread(target=questura_main, args=(r,))

    #t1.start()
    #t2.start()
    t3.start()

    #t1.join()
    #t2.join()
    t3.join()

    while t3.is_alive():#t1.isAlive() or t2.isAlive() or t3.isAlive():
        pass

