"""
    Reads all sections from config and starts workers(metrics collectors)
     accordingly to the module and worker(function) specified in the config
    As well extracts kwargs from config module params section
    As well creates a consumer (db_writer) for each worker
"""
from multiprocessing import Process
from cloudbaseSMS.workers import worker_template as worker
from cloudbaseSMS.consumers import db_writer_template as dbWriter


def run(config):
    """Start processes based on config structure passes in module function and parameters to
    workers and section name and functio name to the consumers.

    :param config: the general config read in the cmd.start -c flag
    :return:
    """
    for section in config.sections():
        if 'module' in [tuple[0] for tuple in config.items(section)]:
            read_metric = Process(target=worker.start_worker,
                                  args=(config[section]['module'], config[section]['worker'],
                                        float(config[section]['interval']), config),
                                  kwargs=(dict({item[0]: eval(item[1])
                                                for item in config.items(section+'_PARAMS')})))
            read_metric.start()
            consumer = Process(target=dbWriter.write,
                               args=(config[section], config[section]['worker'], config))
            consumer.start()
