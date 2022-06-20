import sys

from kafka import KafkaConsumer
import json


from temp_storage_sender import TempStorageSender


class MessageConsumer:
    broker = ""
    topic = ""
    group_id = ""
    logger = None

    def __init__(self, broker, topic, group_id='BDT'):
        self.broker = broker
        self.topic = topic
        self.group_id = group_id
        self.client = TempStorageSender(topic)

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
                try:
                    # send message to google cloud storage
                    self.client.send_message(message, self.topic)

                    # committing message manually after reading from the topic
                    consumer.commit()
                except Exception:
                    print("Could not send message to temp. storage, retrying...")
        except KeyboardInterrupt:
            print("Aborted by user...")
        finally:
            consumer.close()
