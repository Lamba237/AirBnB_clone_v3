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


@app_views.route('/status', methods=['GET'])
def status_OK():
    """return status code: OK"""
    return jsonify({
        "status": "OK"
        })


@app_views.route('/api/v1/stats', methods=['GET'])
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
