import os
import sys
import threading
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the parent directory
from models.message_producer import *
source_layer = os.path.dirname(os.path.dirname(__file__))

broker = 'localhost:9092'  # TODO: modify
topics = ['bank', 'corporate-broker', 'questura']

message_producer_bank = MessageProducer(broker, topics[0])
message_producer_broker = MessageProducer(broker, topics[1])
message_producer_questura = MessageProducer(broker, topics[2])


t1 = threading.Thread(target=message_producer_bank.keep_sending_data_from_dir, args=(source_layer+"/components/reports/", True))
# t2 = threading.Thread(target=assign_id, args=(people,))
# t3 = threading.Thread()

t1.start()

# stop threads after completing the task
# t1.join()
