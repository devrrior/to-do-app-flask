import os
from app import app, db
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy


migrate = Migrate(app, db)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    db.create_all(app=app)
    app.run(host='0.0.0.0', port=port)
