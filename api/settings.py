"""
settings.py
Configuration for Flask app
"""
class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/user'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_POOL_SIZE = 30
    JWT_SECRET_KEY = 'fissionlabs'
    END_POINT = '127.0.0.1:5000'

class Development(Config):
    DEBUG = True


class Testing(Config):
    TESTING = True
    DEBUG = True

class Production(Config):
    DEBUG = False
