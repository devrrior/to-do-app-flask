import os
from flask import Flask
from app.database import db
from app.login_manager import login_manager


from app.auth.auth import auth_bp
from app.general.general import general_bp
from app.tasks.tasks import tasks_bp

app = Flask(__name__)



db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "auth_bp.login"
login_manager.login_message_category = "danger"

app.config.from_object("config.DevelopmentConfig")

app.register_blueprint(auth_bp)
app.register_blueprint(general_bp)
app.register_blueprint(tasks_bp)
