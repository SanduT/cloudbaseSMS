"""
    run to setup module, use with smspls -c <config_path> (optional, sample config will be used)
    sample config in project
"""
from setuptools import setup

setup(
    pbr=True,
    name="cloudbaseSMS",
    version="1.0.1",
    author="Tudor Sandu",
    description="""
Cloudbase assignment
""",
    packages=['cloudbaseSMS', 'cloudbaseSMS.consumers',
              'cloudbaseSMS.workers', 'cloudbaseSMS.runnables', 'cloudbaseSMS.cmd', 'cloudbaseSMS.api','cloudbaseSMS.drivers','cloudbaseSMS.drivers.influxDB'],
    install_requires=['pika', 'configparser', 'influxdb', 'multiprocessing', 'flask'],
    entry_points={
        'console_scripts': [
            'smspls = cloudbaseSMS.cmd.start:main',
        ],
    }
)
