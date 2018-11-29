import os

class Config(object):
    DEBUG = True
    SECRET_KEY = 'super-secret'
    JWT_SECRET_KEY = SECRET_KEY


class DevelopmentConfig(Config):
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = ""


class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    JWT_SECRET_KEY = os.environ.get('SECRET_KEY')


config = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
