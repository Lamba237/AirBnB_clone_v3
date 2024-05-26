#!/usr/bin/python3
"""
This method returns a json status: Ok
"""

from models import storage
from api.v1.views import app_views
from flask import jsonify
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', method='[GET]')
def status_OK():
    """return status code: OK"""
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', method='[GET]')
def stats():
    """retrieves the number of each objects by type:"""
    stats = {
            "amenities": storage.count(Amenity),
            "cities": storage.count(City),
            "places": storage.count(Place),
            "reviews": storage.count(Review),
            "states": storage.count(State),
            "users": storage.count(User)
            }
    return jsonify(stats)


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
