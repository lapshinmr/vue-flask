import os
from .config import configurations
from flask import Flask, current_app, send_file
# from flask_cors import CORS


def create_app(config_name):
    app = Flask(__name__, static_folder="../dist/static")
    app.config.from_object(configurations[config_name])
    configurations[config_name].init_app(app)
    # CORS(app, resources={r"/api/*": {"origins": "*"}})

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    @app.route('/')
    def index():
        dist_dir = current_app.config['DIST_DIR']
        entry = os.path.join(dist_dir, 'index.html')
        return send_file(entry)

    return app
