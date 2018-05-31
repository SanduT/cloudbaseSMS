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
