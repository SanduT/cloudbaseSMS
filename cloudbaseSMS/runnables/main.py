from cloudbaseSMS.workers import  worker_template as worker
from cloudbaseSMS.consumers import db_writer_template as dbWriter
from multiprocessing import Process
from influxdb import InfluxDBClient
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()



def run(config):
    for section in config.sections():
        if 'module' in [tuple[0] for tuple in config.items(section)]:
            w = Process(target=worker.start_worker, args=(config[section]['module'], config[section]['worker'], float(config[section]['interval'])), kwargs=(dict({item[0]: eval(item[1]) for item in config.items(section+'_PARAMS')})))
            w.start()
            client = InfluxDBClient('localhost', 8086, 'root', 'root', 'smsMetrics')
            c = Process(target=dbWriter.write,args=(config[section],config[section]['worker'],client,channel))
            c.start()