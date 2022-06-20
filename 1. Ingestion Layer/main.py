from services.get_data_from_redis import *
from services.send_data_to_kafka import *

to_send = get_dicts_from_redis()  # list of tuples (topic,message)
send_messages(to_send)

pass