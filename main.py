from metricas import Metricas
from queue import Queue
from db import DataBase

db = DataBase()
queue = Queue()

metricas = Metricas.detectar_anomalias(Metricas)
Queue.send_msgs_queue(Queue, metricas)
db.insert_metricas_db(metricas)






