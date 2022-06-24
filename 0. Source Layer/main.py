from services import send_data_to_redis as s
from time import sleep
sleep(90)  # data generator needs to run first

while True:
    s.send()
    sleep(10)
