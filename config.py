import os
# AWS S3 parameter
# S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format(Config.AWS_BUCKET_NAME)

SECRET_KEY = os.urandom(32)
DEBUG = True
PORT = 5000

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or os.urandom(32)
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
    AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
    AWS_BUCKET_NAME= os.getenv('AWS_BUCKET_NAME')
    BT_MERCHANT_ID = os.getenv('BT_MERCHANT_ID')
    BT_PUBLIC_KEY = os.getenv('BT_PUBLIC_KEY')
    BT_PRIVATE_KEY= os.getenv('BT_PRIVATE_KEY')
    OAUTH_CLIENT_ID = os.getenv('OAUTH_CLIENT_ID')
    OAUTH_CLIENT_SECRET = os.getenv("OAUTH_CLIENT_SECRET")


class ProductionConfig(Config):
    DEBUG = False
    ASSETS_DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    ASSETS_DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    ASSETS_DEBUG = False

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    ASSETS_DEBUG = True
