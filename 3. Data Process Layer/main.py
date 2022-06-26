import json

from services.temp_storage_retriever import BucketRetriever

statement_bucket = BucketRetriever("statement-bdt-13")
bank_bucket = BucketRetriever("bank-bdt-13")
broker_bucket = BucketRetriever("broker-bdt-13")
questura_bucket = BucketRetriever("questura-bdt-13")


def work(bucket, kind:str, amount=25):  # TODO: change the name
    bucket.update_bucket_blobs(25)
    l = bucket.get_blobs_content()  # list of dictionaries

    for record in l:
        record = json.dumps(record)
        if kind == 'statement':

        elif kind == 'bank':

        elif kind == 'broker':

        else:
        #  do stuff
        pass
    # delete records


work(statement_bucket)
