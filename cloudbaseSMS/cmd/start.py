"""
    Start function for setup tools console script.
    Sets up a optional config file path flag.
"""
import configparser
import argparse


from cloudbaseSMS.runnables import main as spawn

ARGP = argparse.ArgumentParser()


ARGP.add_argument("-c", "--config", dest='config_file',
                  default='./cloudbaseSMS/config.ini', type=str)
ARGS = ARGP.parse_args()
CONFIG = configparser.ConfigParser()
CONFIG.read(ARGS.config_file)


def main():
    """
    Spawns function from runnables that starts up workers and consumers.
    """
    spawn.run(CONFIG)
