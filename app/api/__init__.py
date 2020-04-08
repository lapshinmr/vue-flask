from flask import Blueprint
from flask_restplus import Api


api = Blueprint('api', __name__)
api_rest = Api(api)


@api.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response


from . import resources
