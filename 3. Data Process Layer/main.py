import json

from services.temp_storage_retriever import BucketRetriever
from models.bank import Bank
from models.broker import Broker
from models.statement import Statement
from models.questura import Questura
from services.send_to_redis import send_record
import threading


statement_bucket = BucketRetriever("statement-bdt-13")
bank_bucket = BucketRetriever("bank-bdt-13")
broker_bucket = BucketRetriever("broker-bdt-13")
questura_bucket = BucketRetriever("questura-bdt-13")


def work(bucket, kind: str, amount=25):  # TODO: change the name
    while True:
        bucket.update_bucket_blobs(amount)
        l = bucket.get_blobs_content()  # list of dictionaries

        for record in l:
            record = json.loads(json.loads(record))
            if kind == 'statement':
                record = Statement(record)
                personal_data, firm, credit = record.make_sense()
                send_record(personal_data, 'personal_data')
                send_record(firm, 'firm')
                send_record(credit, 'credit_data')
            elif kind == 'bank':
                record = Bank(record)
                new_credit, credit_mix, assets, losses = record.make_sense()
                send_record(new_credit, 'new_credit')
                send_record(credit_mix, 'credit_mix')
                send_record(assets, 'assets')
                send_record(losses, 'losses')
            elif kind == 'broker':
                record = Broker(record)
                broker = record.make_sense()
                send_record(broker, 'broker')
            else:  # questura
                record = Questura(record)
                criminal_records = record.make_sense()
                send_record(criminal_records, 'criminal_records')
            # to test on redis: keys (*-report-row)*     [the first * is the table]
        # bucket.delete_blobs()  # delete records  can't do that because of iterator


t1 = threading.Thread(target=work, args=(statement_bucket, 'statement', 50))
t2 = threading.Thread(target=work, args=(bank_bucket, 'bank', 50))
t3 = threading.Thread(target=work, args=(broker_bucket, 'broker', 50))
t4 = threading.Thread(target=work, args=(questura_bucket, 'questura', 50))


t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

