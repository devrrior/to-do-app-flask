import os
from flask import Flask
from app.database import db


from app.auth.auth import auth
from app.general.general import general

app = Flask(__name__)
db.init_app(app)
app.config.from_object("config.DevelopmentConfig")

app.register_blueprint(auth,url_prefix="/")
app.register_blueprint(general,url_prefix="/")