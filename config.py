
class Config(object):
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECRET_KEY = ''

class ProductionConfig(Config):
    DEBUG = False
    # SECRET_KEY = os.environ["SECRET_KEY"]
    # SQLALCHEMY_DATABASE_URI = DB_URI

class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"
