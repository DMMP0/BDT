import json
import os
import sys
import threading
import redis

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # finds the parent directory
from components.document_parser import *
source_layer = os.path.dirname(os.path.dirname(__file__))

path = source_layer + '/components/reports/'
excel = [f for f in os.listdir(path) if f.endswith('.xlsx')]
html = [f for f in os.listdir(path) if f.endswith('.html')]
# tex = [f for f in os.listdir(path) if f.endswith('.tex')]
word = [f for f in os.listdir(path) if f.endswith('.docx')]
txt = [f for f in os.listdir(path) if f.endswith('.txt')]

r = redis.StrictRedis(host='localhost')  # redis object


def send_files_to_redis(filepaths: list, format: str):
    """This function will convert the files into dictionaries with the parser. Once done, it will send them to redis as
    a hash that will have the filename as key and the dictionary as values.
    @:param format: the extension of the file. Possile values: {'docx','excel','html','txt'}"""

    global r  # redis instance
    global path
    for fp in filepaths:
        fp = path+str(fp)
        d = dict()

        # convert into dict
        if format == 'docx':
            d = docx_to_dict(fp)
        elif format == 'excel':
            d = excel_to_dict(fp)
        elif format == 'html':
            d = html_to_dict(fp)
        else:  # elif format == 'txt'
            d = txt_to_dict(fp)

        key = list(d.keys())[0]
        # send to redis
        r.set(name=key, value=json.dumps(d[key]))


t1 = threading.Thread(target=send_files_to_redis,
                      args=(excel, 'excel'))
t2 = threading.Thread(target=send_files_to_redis,
                      args=(html, 'html'))
t3 = threading.Thread(target=send_files_to_redis,
                      args=(word, 'docx'))
t4 = threading.Thread(target=send_files_to_redis,
                      args=(txt, 'txt'))

t1.start()
t2.start()
t3.start()
t4.start()
# stop threads after completing the task
t1.join()
t2.join()
t3.join()
t4.join()
