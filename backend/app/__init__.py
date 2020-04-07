from settings import configurations
from flask import Flask
from flask_cors import CORS


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configurations[config_name])
    configurations[config_name].init_app(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # blueprints
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
