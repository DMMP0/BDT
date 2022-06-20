import os
import random
import sys
from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the parent directory
from credentials.GCS_credentials import credentials_dict
from credentials.GCS_credentials import project_name


class TempStorageSender:
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        credentials_dict
    )
    client = storage.Client(credentials=credentials, project=project_name)

    def __init__(self, bucket_name:str):
        self.bucket = self.client.get_bucket(bucket_name)

    def create_name(self, message: str, topic='', name='report') -> str:
        ris = message[-10:]  # this string will contain the format

        random_string = ''
        for _ in range(20):
            # Considering only upper and lowercase letters
            random_integer = random.randint(97, 97 + 26 - 1)
            flip_bit = random.randint(0, 1)
            # Convert to lowercase if the flip bit is on
            random_integer = random_integer - 32 if flip_bit == 1 else random_integer
            # Keep appending random characters using chr(x)
            random_string += (chr(random_integer))

        return topic + name + ' '+random_string+ris.split('.')[-1]

    def send_message(self, message, topic, name='report'):
        blob = self.bucket.blob(self.create_name(message=message, topic=topic,name=name))
        blob.upload_from_string(data=message)
