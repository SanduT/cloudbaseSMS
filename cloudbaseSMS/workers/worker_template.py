"""This is a general template for a metrics collector that writes data
from a given module and function to a AMQP queue"""
import threading
import pika
import logging
logging.basicConfig(filename='smspls.log', level=logging.INFO)


def set_interval(func, time):
    """Call function every interval

    :param func:Function you want to repeatedly call
    :param time:Interval of function calls(in miliseconds)
    """
    event = threading.Event()
    while not event.wait(time):
        func()


def start_worker(module, function, call_interval, CONF, **params):
    """Worker template function to start a generalised worker

    :param module:Module from where a metrics collection function should be called - ex. psutil
    :param function:Function from that module - ex. cpu_percent
    :param call_interval:Period in with metrics are collected(miliseconds)
    :param CONF: config file set as param in cmd start
    :param params:The function parameters ex:
    psutil.cpu_percent(interval=1, percpu=1) passed as dict from config file.
    """
    module = __import__(module)
    func = getattr(module, function)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=CONF['AMQP']['host']))
    channel = connection.channel()
    channel.queue_declare(queue=function)
    logging.info('Worker ' + function + ' started successfully')

    def send_info():
        """Starts publishing metric information to queue
        :return:
        """
        channel.basic_publish(exchange='', routing_key=function, body=str(func(**params)))

    set_interval(send_info, call_interval)
