from services.get_data_from_redis import *
from services.send_data_to_kafka import *

to_send, redis_keys = get_dicts_from_redis()  # list of tuples (topic,message), keys
send_messages(to_send, redis_keys)



