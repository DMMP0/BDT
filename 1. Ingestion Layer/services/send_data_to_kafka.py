import os
import sys
import threading

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the parent directory
from models.kafka_message_producer import MessageProducer


def send_messages(messages: [], Threading=True):
    """@:param messages: must be a list of tuples (topic,messages)"""
    # Running multiple producers
    broker = 'localhost:9092' # TODO: change
    topics = ['bank', 'broker', 'questura']

    bank_producer = MessageProducer(broker, topics[0])
    broker_producer = MessageProducer(broker, topics[1])
    questura_producer = MessageProducer(broker, topics[2])

    t1 = threading.Thread(target=bank_producer.keep_sending_data, args=(messages,))
    t2 = threading.Thread(target=broker_producer.keep_sending_data, args=(messages,))
    t3 = threading.Thread(target=questura_producer.keep_sending_data, args=(messages,))

    t1.start()
    t2.start()
    t3.start()

    # stop threads after completing the task
    t1.join()
    t2.join()
    t3.join()
