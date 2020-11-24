import pika


class Queue:

    def send_msgs_queue(self, metricas):

        msg = metricas.to_json(index=False, orient='split')

        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='metricas')

        channel.basic_publish(exchange='', routing_key='metricas', body=str(msg))
        print(" [x] Sent " + str(msg))
        connection.close()

