import json
import os
import time
from random import Random

from kafka import KafkaProducer


class MessageProducer:
    broker = ""
    topic = ""
    producer = None

    def __init__(self, broker, topic):
        self.broker = broker
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=self.broker,
                                      value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                                      acks='all',
                                      retries=3)

    def send_msg(self, msg):
        print("sending message...")
        try:
            future = self.producer.send(self.topic, msg)
            self.producer.flush()
            future.get(timeout=60)
            print("message sent successfully...")
            return {'status_code': 200, 'error': None}
        except Exception as ex:
            return ex

    def keep_sending_data_from_dir(self, directory: str, simulation=True):
        data = os.listdir(directory)

        if simulation:  # we only have few files
            while True:
                filename = data[Random().randint(0, len(data)-1)]
                if filename[0:4] != self.topic[0:4]:
                    continue  # not a message from this  producer
                with open(directory+filename, mode='r', encoding='utf-8') as f:
                    try:
                        msg = f.read()
                        self.send_msg(msg)
                    except UnicodeDecodeError:
                        print("Could not decode the file: "+filename)
                time.sleep(2)
        else:   # we are testing with lots of files
            for filename in data:
                if filename[0:4] != self.topic:
                    continue  # not a message from this  producer
                with open(directory + filename, mode='r', encoding='utf-8') as f:
                    try:
                        msg = f.read()
                        self.send_msg(msg)
                    except UnicodeDecodeError:
                        print("Could not decode the file: " + filename)
                time.sleep(2)

