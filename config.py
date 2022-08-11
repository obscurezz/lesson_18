import os


class BaseConfig(object):
    SECRET_KEY = os.urandom(12)
    RESTX_JSON = {'ensure_ascii': False}
    JSON_SORT_KEYS = False
    JSON_AS_ASCII = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    DEBUG = True
    ENV = 'development'
    PORT = 5000
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///movies.db"


class ProdConfig(BaseConfig):
    ENV = 'production'
    PORT = 8080
    SQLALCHEMY_DATABASE_URI = "sqlite:///movies.db"
