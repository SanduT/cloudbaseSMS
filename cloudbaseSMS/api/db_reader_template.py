from influxdb import InfluxDBClient


def read(section,CONF):
    client = InfluxDBClient(CONF['INFLUXDB']['host'], CONF['INFLUXDB']['port'],
                            CONF['INFLUXDB']['username'], CONF['INFLUXDB']['password'],
                            'smsMetrics')
    query="SELECT \"value\" FROM \"smsMetrics\".\"autogen\".\""+section+"\" WHERE time > now() - 1h"
    return str(client.query(query))
