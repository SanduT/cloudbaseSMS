# cloudbaseSMS
A metrics colector for any system.

## The idea
It is designed to be adatpable to any module for collecting metrics.

It contains of a .ini config file where you specify the module and worker(method from module) used for collecting system data.

Based on the config file it creates workers that extract data on given intervals of time and adds them to a RabbitMQ queue.

The information from the queue gets added to a DB (project includes drivers for influxdb)

As well an API is created for the enpoints specified in the .ini file

## Usage
1.Add your desired metrics collector function in the config.ini file, example:
```
[CPU_PERCENTAGE]
module=psutil
worker=cpu_percent
interval=0.05
API_ENDPOINT=/cpu
[CPU_PERCENTAGE_PARAMS]
interval = 0.05
percpu = 1

```
This will create a RabbitMQ queue with the same name as the worker wich will send info in intervals set by the interval field.
You can add as many workers you want.
All parameters should be set under [<section_name>_PARAMS] section of the config file.

Install with:
```
sudo python setyp.py install

```

External dependencies: (if included drivers are used)

```
sudo apt-get update && sudo apt-get install influxdb

```

Run with:
```
smspls -c <config_path>(optional-by default the one from the project folder is being used)

```

This will:
1.Start all the worker processes.

2.Insert data from queues to influxdb.

3.Create API endpoints to be used for retrieving data. (note: to queue an endpoint ex: /cpu you can use cpu/2 to retrieve data from the past 2 hours till now)

## Author

* **Tudor Sandu** 
