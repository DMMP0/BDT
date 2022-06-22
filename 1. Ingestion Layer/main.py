from services.get_data_from_redis import *
from services.send_data_to_kafka import *
from time import sleep

while True:
    to_send, redis_keys = get_dicts_from_redis()  # list of tuples (topic,message), keys
    if to_send is False or redis_keys is False:  # no new keys
        print("Waiting for new records...\n")
        sleep(10)
        continue
    send_messages(to_send, redis_keys)
    sleep(5)
