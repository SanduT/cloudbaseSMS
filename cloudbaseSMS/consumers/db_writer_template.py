#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
from influxdb import InfluxDBClient
from datetime import datetime


client = InfluxDBClient('localhost', 8086, 'root', 'root', 'smsMetrics2')
client.create_database('smsMetrics2')
channel.queue_declare(queue='virtual_memory')

def printto(ch, method, properties, body):
    print (dict(body))

def write_to_db(ch, method, properties, body):
    print(body)
    client.write_points([
    {
        "measurement": 'virtual_memory',
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "fields": {
            "value": float(body)
        }
    }
    ])


channel.basic_consume(printto,
                      queue='virtual_memory',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()