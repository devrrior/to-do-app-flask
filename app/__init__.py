# TODO Añadir test unitarios
# TODO servidor de correos
from flask import Flask
from app.models import db
from app.auth.form_auth import login_manager

from app.auth.auth import auth_bp
from app.general.general import general_bp
from app.tasks.tasks import tasks_bp

app = Flask(__name__)


app.config.from_object("config.ProductionConfig")


db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "auth_bp.login"
login_manager.login_message_category = "danger"

app.register_blueprint(auth_bp)
app.register_blueprint(general_bp)
app.register_blueprint(tasks_bp)
