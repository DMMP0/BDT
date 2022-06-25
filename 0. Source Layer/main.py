from services import send_data_to_redis as s
from time import sleep

while True:
    s.send()
    sleep(10)
