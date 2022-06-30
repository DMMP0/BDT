import json
import os
import sys
import threading
import redis

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the parent directory
from components.document_parser import *

source_layer = os.path.dirname(os.path.dirname(__file__))
r = redis.StrictRedis(host='redis')  # redis object. host='localhost')#
# host='redis' assumes docker, use host = localhost for localhost


def send():
    path = source_layer + '/components/reports/'
    excel = [f for f in os.listdir(path) if f.endswith('.xlsx')]
    html = [f for f in os.listdir(path) if f.endswith('.html')]
    word = [f for f in os.listdir(path) if f.endswith('.docx')]
    txt = [f for f in os.listdir(path) if f.endswith('.txt')]
    csv = [f for f in os.listdir(path) if f.endswith('.csv')]

    def send_files_to_redis(filepaths: list, formato: str):
        """This function will convert the files into dictionaries with the parser.
        Once done, it will send them to redis as a hash that will have the filename as key and the dictionary as values.
        @:param format: the extension of the file. Possible values: {'docx','excel','html','txt','csv'}"""

        global r  # redis instance

        if not filepaths:
            print("No new files so far.\n")
            return
        for fp in filepaths:
            sent = False
            fp = path + str(fp)
            try:
                while not sent:

                    # d = dict()

                    # convert into dict
                    if formato == 'docx':
                        d = docx_to_dict(fp)
                    elif formato == 'excel':
                        d = excel_to_dict(fp)
                    elif formato == 'html':
                        d = html_to_dict(fp)
                    elif formato == 'txt':
                        d = txt_to_dict(fp)
                    else:  # elif formato == 'csv':
                        d = csv_to_dict(fp)


                    key = list(d.keys())[0]

                    # send to redis
                    sent = r.set(name=key, value=json.dumps(d[key])[:-1]+'}')
                    if not sent:
                        print(key + 'not sent.\tRetrying...')
                os.remove(fp)
            except Exception:
                print("Error while reading the file")
        print("Batch of " + formato + " sent succesfully")

    t1 = threading.Thread(target=send_files_to_redis,
                          args=(excel, 'excel'))
    t2 = threading.Thread(target=send_files_to_redis,
                          args=(html, 'html'))
    t3 = threading.Thread(target=send_files_to_redis,
                          args=(word, 'docx'))
    t4 = threading.Thread(target=send_files_to_redis,
                          args=(txt, 'txt'))
    t5 = threading.Thread(target=send_files_to_redis,
                          args=(csv, 'csv'))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    # stop threads after completing the task
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
