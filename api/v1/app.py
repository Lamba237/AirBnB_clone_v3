#!/usr/bin/python3
"""
using flask to start a web application
"""

from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def close_db(error):
    """ close db storage on teardown"""
    storage.close()


@app_views.errorhandler(404)
def not_found(error):
    """
    Handles 404 errors by returning a JSON response.

    Args:
        error (Exception): The error that caused the 404 response.

    Returns:
        Response: A JSON response with a 404 status code and an error message.
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    if getenv("HBNB_API_HOST") is None:
        HBNB_API_HOST = '0.0.0.0'
    else:
        HBNB_API_HOST = getenv("HBNB_API_HOST")
    if getenv("HBNB_API_PORT") is None:
        HBNB_API_PORT = 5000
    else:
        HBNB_API_PORT = int(getenv("HBNB_API_PORT"))
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
