#!/usr/bin/python3
'''This method returns a json status: Ok'''
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
    return jsonify({'status':   'Good boy'})


@app_views.route('/api/v1/stats', methods=['GET'])
def stats():
    """retrieves the number of each objects by type:"""
    stat = {
            "amenities": Amenity,
            "cities": City,
            "places": Place,
            "reviews": Review,
            "states": State,
            "users": User
            }
    for key in stat:
        stat[key] = storage.count(stat[key])
    return jsonify(stat)
