from flask import jsonify
from . import api


@api.route('/')
def index():
    return jsonify('Hello')

