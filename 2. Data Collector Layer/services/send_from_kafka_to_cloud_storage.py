import os
import sys
import threading

# finds the source directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # finds the directory
from models.message_consumer import MessageConsumer


def send_messages():
    """@:param messages: must be a list of tuples (topic,messages)"""
    # Running multiple producers
    broker = 'localhost:9092'  # TODO: change
    topics = ['bank', 'broker', 'questura', 'statement']
    group_ids = ['bank-consumer', 'broker-consumer', 'questura-consumer', 'statement-consumer']

    bank_consumer = MessageConsumer(broker, topics[0], group_ids[0])
    broker_consumer = MessageConsumer(broker, topics[1], group_ids[1])
    questura_consumer = MessageConsumer(broker, topics[2], group_ids[2])
    statement_consumer = MessageConsumer(broker, topics[3], group_ids[3])

    t1 = threading.Thread(target=bank_consumer.activate_listener)
    t2 = threading.Thread(target=broker_consumer.activate_listener)
    t3 = threading.Thread(target=questura_consumer.activate_listener)
    t4 = threading.Thread(target=statement_consumer.activate_listener)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    # stop threads after completing the task
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    while t1.is_alive() and t2.is_alive() and t3.is_alive():
        pass

    # join lists in order not to delete the error keys
