#!/usr/bin/python3
""" import flask packages"""

from flask import Blueprint
from . import views

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
