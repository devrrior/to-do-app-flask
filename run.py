from app import app, db, User, Task
from flask_script import Shell


def make_shell_context():
    return dict(app=app, db=db, User=User, Task=Taks)


if __name__ == "__main__":
    # app.add_command('shell', Shell(make_context=make_shell_context()))
    db.create_all(app=app)
    app.run(host='0.0.0.0')
