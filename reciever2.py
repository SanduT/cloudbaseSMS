#!/usr/bin/env python
import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
data = 0


channel.queue_declare(queue='net_io_counters')

def callback(ch, method, properties, body):
    data = body

channel.basic_consume(callback,
                      queue='net_io_counters',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()