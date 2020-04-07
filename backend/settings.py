import os


basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    JSONIFY_PRETTYPRINT_REGULAR = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGODB_SETTINGS = [
        {
            "ALIAS": "default",
            "DB":    'data',
            "HOST": 'localhost',
            "PORT": 27017,
            'connect': False
        }
    ]

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
