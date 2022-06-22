from services import send_from_kafka_to_cloud_storage as gcs
from time import sleep

while True:
    gcs.send_messages()

    print("No new messages so far, waiting...\n")
    sleep(60)

# gsutil -m rm -r gs://questura-bdt-13/\* to remove all files into google cloud storage
