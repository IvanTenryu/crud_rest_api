class Config(object):
  DEBUG = False
  TESTING = False
  SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3366/test'

class DevelopmentConfig(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3366/test'
  SQLALCHEMY_ECHO = False

class TestingConfig(Config):
  TESTING = True
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3366/test'
  SQLALCHEMY_ECHO = False

