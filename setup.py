from setuptools import setup

setup(
    pbr=True,
    name="cloudbaseSMS",
    version="0.0.2",
    author="Tudor Sandu",
    description="""
Cloudbase assignment
""",
    packages=['cloudbaseSMS', 'cloudbaseSMS.consumers','cloudbaseSMS.workers','cloudbaseSMS.runnables','cloudbaseSMS.cmd'],
    install_requires=['pika', 'configparser'],
    entry_points={
        'console_scripts': [
            'smspls = cloudbaseSMS.cmd.start:main',
        ],
    }
)
