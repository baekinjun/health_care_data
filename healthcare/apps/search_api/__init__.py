from flask import Blueprint, request
from flask_restful import Api
from .urls import url_patterns

search_api = Blueprint('search_api', __name__, url_prefix='/api_v1/search')
api = Api(search_api)

for view_class, route in url_patterns:
    api.add_resource(view_class, route)