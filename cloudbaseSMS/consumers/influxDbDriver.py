from datetime import datetime
def write(body,client,moduleName):
    client.write_points([
        {
            "measurement": moduleName,
            "time": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
            "fields": {
                "value": body
            }
        }
    ])