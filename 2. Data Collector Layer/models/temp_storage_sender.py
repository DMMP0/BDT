import json
import os
import random
import sys
from google.cloud import storage

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the parent directory


# gsutil -m rm -r gs://questura-bdt-13/\* to remove all files into google cloud storage

class TempStorageSender:
    client = storage.Client.from_service_account_info(info=json.loads(os.environ['credentials']))

    # .from_service_account_json(json_credentials_path='/home/dmmp/Documents/GitHub/BDT/credentials/bdt-project-200-6164fe338b7d.json')

    def __init__(self, bucket_name: str):
        self.bucket = self.client.get_bucket(bucket_name)

    def create_name(self, message: str, topic='', name='-report-row-') -> str:
        ris = message[-4:]  # this string will contain the format

        random_string = ''
        for _ in range(20):
            # Considering only upper and lowercase letters
            random_integer = random.randint(97, 97 + 26 - 1)
            flip_bit = random.randint(0, 1)
            # Convert to lowercase if the flip bit is on
            random_integer = random_integer - 32 if flip_bit == 1 else random_integer
            # Keep appending random characters using chr(x)
            random_string += (chr(random_integer))

        return topic + name + ' ' + random_string + '-' + ris

    def send_message(self, message, topic, name='report'):
        blob = self.bucket.blob(blob_name=self.create_name(message=message, topic=topic, name=name))
        blob.upload_from_string(data=message)
