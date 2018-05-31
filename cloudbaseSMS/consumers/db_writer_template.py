#!/usr/bin/env python

from cloudbaseSMS.consumers.influxDbDriver import write as driver


def write(moduleName,queueName,client,channel):
    def write_to_db(ch, method, properties, body):
        driver(body,client,moduleName)
    print(queueName)
    channel.queue_declare(queue=queueName)
    channel.basic_consume(write_to_db,
                      queue=queueName,
                      no_ack=True)
    print('started consuming')
    channel.start_consuming()