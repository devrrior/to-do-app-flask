from app import create_app, db, User, Task
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from flask_sqlalchemy import SQLAlchemy
from config import config


def make_shell_context():
    return dict(app=app, db=db, User=User, Task=Task)


config_class = config["production"]
app = create_app(config_class)
migrate = Migrate(app, db)

if __name__ == "__main__":
    manager = Manager(app)
    db.create_all(app=app)

    manager.add_command("shell", Shell(make_context=make_shell_context))

    @manager.command
    def test():
        import unittest
        tests = unittest.TestLoader().discover('tests')
        unittest.TextTestRunner().run(tests)

    manager.add_command("db", MigrateCommand)

    manager.run()
