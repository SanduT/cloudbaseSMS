"""
    DB driver to help abstract data and business layers
"""
from datetime import datetime
from influxdb import InfluxDBClient


def write(body, sectionName, CONF):
    """Writes given input to Influx

    :param body: Points to write to db
    :param sectionName: Serves as a name for the db table
    :param CONF: Credentials, passwords and such
    :return:
    """
    client = InfluxDBClient(CONF['INFLUXDB']['host'], CONF['INFLUXDB']['port'],
                            CONF['INFLUXDB']['username'], CONF['INFLUXDB']['password'],
                            'smsMetrics')
    client.write_points([
        {
            "measurement": sectionName,
            "time": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
            "fields": {
                "value": body
            }
        }
    ])


def read(section, CONF, time):
    """Reads from influx return query as string
    :param section: name of the db table
    :param CONF: config file for setting influx credentials and such
    :param time: time to query from db
    :return:
    """
    client = InfluxDBClient(CONF['INFLUXDB']['host'], CONF['INFLUXDB']['port'],
                            CONF['INFLUXDB']['username'], CONF['INFLUXDB']['password'],
                            'smsMetrics')
    query = "SELECT \"value\" FROM \"smsMetrics\".\"autogen\".\""+section+"\" WHERE time >now()-"+time+"h"
    return str(client.query(query))
