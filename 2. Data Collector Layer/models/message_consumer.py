import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # finds the directory

from temp_storage_sender import TempStorageSender
from kafka import KafkaConsumer
import json


class MessageConsumer:
    broker = ""
    topic = ""
    group_id = ""
    logger = None

    def __init__(self, broker, topic, group_id='BDT'):
        self.broker = broker
        self.topic = topic
        self.group_id = group_id
        self.client = TempStorageSender(topic + "-bdt-13")

    def activate_listener(self):
        consumer = KafkaConsumer(bootstrap_servers=self.broker,
                                 group_id=self.group_id,
                                 consumer_timeout_ms=60000,
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=False,
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')))

        consumer.subscribe(self.topic)
        print("consumer is listening....")
        try:
            for message in consumer:  # TODO: not sure about this yet
                # send the message to the persistence layer

                self.client.send_message(message.value, self.topic)

                consumer.commit()
                print("message sent successfully")

        except KeyboardInterrupt:
            print("Aborted by user...")
        finally:
            consumer.close()
