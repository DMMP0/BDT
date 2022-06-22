import json
import time


from kafka import KafkaProducer
import redis


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
        self.__redis_error_keys = []

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

    def send_gathered_data(self, list_of_tuples):
        r = redis.StrictRedis()
        for el in list_of_tuples:
            if el[0] != self.topic:
                continue  # not a message from this  producer
            ris = self.send_msg(json.dumps(el[1])+el[2].decode('utf-8')[-4:])
            if ris['status_code'] != 200:
                print(ris['error'])
                self.__redis_error_keys.append(el[2])
            time.sleep(2)

    def get_error_keys(self):
        return self.__redis_error_keys
