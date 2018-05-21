import configparser
from workers import  worker_template as worker
from multiprocessing import Process


config = configparser.ConfigParser()
config.read('config.ini')

if __name__ == '__main__':
    for section in config.sections():
        if 'module' in [tuple[0] for tuple in config.items(section)]:
        # print(config[section]['module'])
        # print(config[section]['worker'])
        # print(config[section]['interval'])
        # print({item[0]: eval(item[1]) for item in config.items(section+'_PARAMS')})
            p = Process(target=worker.start_worker, args=(config[section]['module'], config[section]['worker'], int(config[section]['interval'])), kwargs=(dict({item[0]: eval(item[1]) for item in config.items(section+'_PARAMS')})))
            p.start()