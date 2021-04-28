from dotenv import load_dotenv
import os
load_dotenv()


class Config(object):
    DEBUG = False
    TEST = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI")


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI_DEV")


class TestConfig(Config):
    TEST = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db_test.sqlite3"


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "test": TestConfig,
}
