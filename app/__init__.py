import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="../app/views/")
app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)

from app.routes.index_routes import *
from app.routes.registrations_routes import *
from app.routes.login_routes import *