#!/usr/bin/env python
import pika
from metricas import Metricas

met = Metricas
msg = Metricas.detectarAnomalias(met).to_json(index=False, orient='split')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body=str(msg))
print(" [x] Sent "+str(msg))
connection.close()