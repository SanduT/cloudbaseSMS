from cloudbaseSMS.workers import  worker_template as worker
from multiprocessing import Process




def run(config):
    for section in config.sections():
        if 'module' in [tuple[0] for tuple in config.items(section)]:
            p = Process(target=worker.start_worker, args=(config[section]['module'], config[section]['worker'], float(config[section]['interval'])), kwargs=(dict({item[0]: eval(item[1]) for item in config.items(section+'_PARAMS')})))
            p.start()

