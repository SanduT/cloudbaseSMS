"""
    A reader module. reads data from the db through a driver.
    If api endpoint is the same as in the config file it returns
    it's corresponding function call to read table from db
"""
import logging
from flask import Flask
from cloudbaseSMS.drivers.influxDB import influxDbDriver as driver
APP = Flask(__name__)
logging.basicConfig(filename='smspls.log', level=logging.INFO)


def start(config):
    """Starts the api and listens for endpoints from the config file

    :param config: The config file given as a cmd flag
    :return:
    """
    @APP.route('/<name>/<time>')
    def my_view_func(name, time):
        """Defines flask endpoints and calls read function for the appropriate db metrics
        :param name: endpoint used
        :param time: time passed to query in hours ex: 1 will query all data from 1 hour ago till now
        :return:
        """
        for section in config.sections():
            if '/'+str(name) in [tuple[1] for tuple in config.items(section)]:
                return driver.read(section, config, time)

    logging.info('API AVAILABE')
    APP.run(port=config['API']['port'])
