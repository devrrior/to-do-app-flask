import os
# from dotenv import load_dotenv
# load_dotenv()


class Config(object):
    DEBUG = False
    TEST = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI")


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI_DEV")


class TestConfig(Config):
    TEST = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db_test.sqlite3"
