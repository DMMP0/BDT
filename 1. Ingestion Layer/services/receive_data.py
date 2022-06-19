import os
import sys
import threading

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the parent directory
from models.message_consumer import MessageConsumer

# Running multiple consumers
broker = 'localhost:9092' # TODO: change
topics = ['bank', 'broker', 'questura']
group_ids = ['bank-consumer', 'broker-consumer', 'questura-consumer']

bank_consumer = MessageConsumer(broker, topics[0], group_ids[0])
broker_consumer = MessageConsumer(broker, topics[1], group_ids[1])
questura_consumer = MessageConsumer(broker, topics[2], group_ids[2])

t1 = threading.Thread(target=bank_consumer.activate_listener)
t2 = threading.Thread(target=broker_consumer.activate_listener)
t3 = threading.Thread(target=questura_consumer.activate_listener)

t1.start()
t2.start()
t3.start()

# stop threads after completing the task
t1.join(20)
t2.join(20)
t3.join(20)
