"""
    A consumer template that reads data from given amqp
    queue and adds metrics to the db.
"""
import pika
import logging
from cloudbaseSMS.drivers.influxDB import influxDbDriver as driver
logging.basicConfig(filename='smspls.log', level=logging.INFO)


def write(sectionName, queueName, CONF):
    """A generalised write to db consumer tamplate with decoupled data layer connection.

    :param sectionName: Name of the section servers as name of the table in the db
    :param queueName: Name of the queue where the data is extracted from
    :param CONF: A conf file for credentials hosts and such
    :return:
    """
    def write_to_db(ch, method, properties, body):
        """A helper function that writes to db thorugh a driver.
        :param body:
        :return:
        """
        driver.write(body, sectionName, CONF)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=CONF['AMQP']['host']))
    channel = connection.channel()
    channel.queue_declare(queue=queueName)
    channel.basic_consume(write_to_db,
                          queue=queueName,
                          no_ack=True)
    logging.info('Consumer ' + sectionName + ' started successfully')
    channel.start_consuming()
