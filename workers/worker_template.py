import pika
import threading


def set_interval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()


def start_worker(module,function,interval1,**params):

    module = __import__(module)
    func = getattr(module, function)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    print (params);
    channel.queue_declare(queue=function)

    def send_info():
        channel.basic_publish(exchange='',
                      routing_key=function,
                      body=str(func(**params)))

    set_interval(send_info, interval1)
    connection.close()


