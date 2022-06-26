import json
import os
import json

from google.cloud import storage


# gsutil -m rm -r gs://questura-bdt-13/\* to remove all files into google cloud storage

class BucketRetriever:
    client = storage.Client.from_service_account_json(json_credentials_path='/home/dmmp/Documents/GitHub/BDT/credentials/bdt-project-200-6164fe338b7d.json')
    # .from_service_account_info(info=json.loads(os.environ['CREDENTIALS']))
    # .from_service_account_json(json_credentials_path='/home/dmmp/Documents/GitHub/BDT/credentials/bdt-project-200-6164fe338b7d.json')

    def __init__(self, bucket_name: str):
        self.__bucket = self.client.get_bucket(bucket_name)
        self.blobs = None

    def update_bucket_blobs(self, max_number: -1):
        if max_number < 1:
            self.blobs = self.client.list_blobs(bucket_or_name=self.__bucket.name)
        else:
            self.blobs = self.client.list_blobs(bucket_or_name=self.__bucket.name, max_results=max_number)

    def get_blobs_content(self) -> list:
        """@:returns a list of dictionaries"""

        ris = list()

        for blob in self.blobs:
            ris.append(json.dumps(blob.download_as_text()))


        return ris

    def delete_blobs(self, lst=None):

        if lst is None:
            lst = self.blobs

        for blob in lst:
            blob.delete()