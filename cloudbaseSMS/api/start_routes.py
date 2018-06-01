from flask import Flask
app = Flask(__name__)
from cloudbaseSMS.api import db_reader_template



def start(config):
    @app.route('/<name>')
    def my_view_func(name):
        for section in config.sections():
            if '/'+str(name) in [tuple[1] for tuple in config.items(section)]:
                return db_reader_template.read(section,config)
    app.run(port=3333)