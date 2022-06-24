from services import send_data_to_redis as s
from time import sleep
sleep(130)

while True:
    s.send()
    sleep(10)
