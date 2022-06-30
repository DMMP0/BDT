import json
import random

import redis

r = redis.StrictRedis(host='redis')  # redis object. host='localhost')#


# host='redis' assumes docker, use host = localhost for localhost

def create_name(topic='', name='-report-row') -> str:
    random_string = ''
    for _ in range(20):
        # Considering only upper and lowercase letters
        random_integer = random.randint(97, 97 + 26 - 1)
        flip_bit = random.randint(0, 1)
        # Convert to lowercase if the flip bit is on
        random_integer = random_integer - 32 if flip_bit == 1 else random_integer
        # Keep appending random characters using chr(x)
        random_string += (chr(random_integer))

    return '(' + topic + name + ')' + random_string


def send_record(record: dict, topic: str):
    name = create_name(topic)
    not_sent = False
    while not bool(not_sent):
        not_sent = r.set(name, json.dumps(record))  # it will be 0 if nothing was added
    print("Message sent successfully")
