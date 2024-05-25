#!/usr/bin/python3
""" This method returns a json status: Ok"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', method='[GET]')
def status_OK():
    """return status code: OK"""
    return jsonify({"status": "OK"})
