import json
import time


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

    def keep_sending_data(self, list_of_tuples):
        for el in list_of_tuples:
            if el[0] != self.topic:
                continue  # not a message from this  producer
            self.send_msg(json.dumps(el[1]))
            time.sleep(2)
