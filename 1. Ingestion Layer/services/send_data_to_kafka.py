import os
import sys
import threading
import redis

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the parent directory
from models.kafka_message_producer import MessageProducer


def send_messages(messages: [], redis_keys: []):
    """@:param messages: must be a list of tuples (topic,messages)"""
    # Running multiple producers
    broker = 'kafka-server'
    topics = ['bank', 'broker', 'questura', 'statement']
    r = redis.StrictRedis(host='redis')

    bank_producer = MessageProducer(broker, topics[0])
    broker_producer = MessageProducer(broker, topics[1])
    questura_producer = MessageProducer(broker, topics[2])
    statement_producer = MessageProducer(broker, topics[3])

    t1 = threading.Thread(target=bank_producer.send_gathered_data, args=(messages,))
    t2 = threading.Thread(target=broker_producer.send_gathered_data, args=(messages,))
    t3 = threading.Thread(target=questura_producer.send_gathered_data, args=(messages,))
    t4 = threading.Thread(target=statement_producer.send_gathered_data, args=(messages,))

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

    # concatenate all the keys gathered so far with the error keys
    redis_keys = redis_keys + \
         bank_producer.get_error_keys() + \
         broker_producer.get_error_keys() + \
         questura_producer.get_error_keys() + statement_producer.get_error_keys()

    if not redis_keys:  # no keys on redis
        return

    # the keys with an error will be duplicates
    # remove duplicates, so we get only keys without an error
    redis_keys = list(set(redis_keys))

    # delete elements that were successfully passed
    r.delete(*redis_keys)
