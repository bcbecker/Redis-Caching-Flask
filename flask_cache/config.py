import os

class Config:
    CACHE_TYPE = os.environ.get('CACHE_TYPE', "CACHE_TYPE does not exist")
    CACHE_HOST = os.environ.get('CACHE_HOST', "CACHE_HOST does not exist")
    CACHE_PORT = os.environ.get('CACHE_PORT', "CACHE_PORT does not exist")
    CACHE_DB= os.environ.get('CACHE_DB', "CACHE_DB does not exist")
    CACHE_URL= os.environ.get('CACHE_URL', "CACHE_URL does not exist")
    CACHE_TIMEOUT= os.environ.get('CACHE_TIMEOUT', "CACHE_TIMEOUT does not exist")
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True