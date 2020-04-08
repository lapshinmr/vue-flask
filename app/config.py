import os


basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    JSONIFY_PRETTYPRINT_REGULAR = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    DIST_DIR = os.path.join(ROOT_DIR, 'dist')
    MONGODB_SETTINGS = [
        {
            "ALIAS": "default",
            "DB":    'data',
            "HOST": 'localhost',
            "PORT": 27017,
            'connect': False
        }
    ]

    print(DIST_DIR)
    if not os.path.exists(DIST_DIR):
        raise Exception('DIST_DIR not found: {}'.format(DIST_DIR))

    @staticmethod
    def init_app(app):
        pass


class Production(BaseConfig):
    PRODUCTION = True


class Development(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True


class Testing(BaseConfig):
    DEBUG = True
    TESTING = True
    MONGODB_SETTINGS = [
        {
            "ALIAS": "default",
            "DB":    'data_test',
            "HOST": 'localhost',
            "PORT": 27017,
            'connect': False
        }
    ]


configurations = {
    'D': Development,
    'P': Production,
    'T': Testing
}
