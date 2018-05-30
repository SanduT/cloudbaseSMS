import configparser
import argparse

import mytwitter.config

from  cloudbaseSMS.runnables import main as spawn

from mytwitter import log

# CONF = mytwitter.config.CONF

argp = argparse.ArgumentParser()
# Add an optional string argument 'config'
argp.add_argument ("-c", "--config", dest='config_file', default='./cloudbaseSMS/config.ini', type=str);
args = argp.parse_args()
config = configparser.ConfigParser()
config.read(args.config_file)



def main():
    # args = parser.parse_args()
    #
    # CONF.load_config(args.config_path)
    # log.configure_logging()
    spawn.run(config)
