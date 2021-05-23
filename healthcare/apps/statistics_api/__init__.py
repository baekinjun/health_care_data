from flask import Blueprint, request
from flask_restful import Api
from .urls import url_patterns

statics_api = Blueprint('statics_api', __name__, url_prefix='/api_v1/statics')
api = Api(statics_api)

for view_class, route in url_patterns:
    api.add_resource(view_class, route)

