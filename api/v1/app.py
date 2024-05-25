#!/usr/bin/python3
""" using flask to start a web application """

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
    """ close db storage on teardown"""
    storage.close()


if __name__ == '__main__':
    host_name = getenv('HBNB_API_HOST', '0.0.0.0')
    host_port = getenv('HBNB_API_PORT', '5000')
    app.run(host=host_name, port=host_port, threaded=True)
