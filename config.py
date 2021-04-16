import os

class Config(object):
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"
    SECRET_KEY = "\x8bm\r\xa6v\x88\xe4'\xebt\x19W\xc3\x84\x92 \xaf\xac:\x9e\xc1D\x96\xcc"

class ProductionConfig(Config):
    DEBUG = False
    # SECRET_KEY = os.environ["SECRET_KEY"]
    # SQLALCHEMY_DATABASE_URI = DB_URI

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"
