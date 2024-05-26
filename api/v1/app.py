#!/usr/bin/python3
"""
using flask to start a web application
"""

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
    """ close db storage on teardown"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """
    Handles 404 errors by returning a JSON response.

    Args:
        error (Exception): The error that caused the 404 response.

    Returns:
        Response: A JSON response with a 404 status code and an error message.
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app_views.run(debug=True)
