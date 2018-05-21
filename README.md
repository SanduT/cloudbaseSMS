# cloudbaseSMS
A metrics colector for any system.

## The idea
It is designed to be adatpable to any module for collecting metrics.

It contains of a .ini config file where you specify the module and worker(method from module) used for collecting system data.

Based on the config file it creates workers that extract data on given intervals of time and adds them to a RabbitMQ queue.


## Usage
1.Add your desired metrics collector function in the config.ini file, example:
```
[CPU_PERCENTAGE]
module=psutil
worker=cpu_percent
interval=2
API_ENDPOINT=/cpu
[CPU_PERCENTAGE_PARAMS]
interval = 2
percpu = 1

```
This will create a RabbitMQ queue with the same name as the worker wich will send info in intervals set by the interval field.
You can add as many workers you want.
All parameters should be set under [<section_name>_PARAMS] section of the config file.

Run with:
```
python main.py

```
This will start all the worker processes.

2.Check queues for data.

3.???

4.$$profit

## Author

* **Tudor Sandu** 
