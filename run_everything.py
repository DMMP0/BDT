import multiprocessing
import os

source_layer_generator = "./0. Source Layer/data_generation.py"
source_layer = './0. Source Layer/main.py'
ingestion_layer = './1. Ingestion Layer/main.py'
data_collector_layer = './2. Data Collector Layer/main.py'
data_process_layer = './3. Data Process Layer/main.py'
data_storage_layer = './4. Data Storage Layer/main.py'

p1 = multiprocessing.Process(target=os.system, args=('python ' + source_layer_generator,))
p2 = multiprocessing.Process(target=os.system, args=('python ' + source_layer,))
p3 = multiprocessing.Process(target=os.system, args=('python ' + ingestion_layer,))
p4 = multiprocessing.Process(target=os.system, args=('python ' + data_collector_layer,))
p5 = multiprocessing.Process(target=os.system, args=('python ' + data_process_layer,))
p6 = multiprocessing.Process(target=os.system, args=('python ' + data_storage_layer,))

p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()

p1.join()
p2.join()
p3.join()
p4.join()
p5.join()
p6.join()
