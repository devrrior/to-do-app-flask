from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=True)
    description = db.Column(db.String(140), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __str__(self):
        return f"Id:{self.id}, title:{self.title}, description:{self.description}, user_id:{self.user_id}"

    @property
    def little_title(self):
        if len(self.title) > 19:
            return self.title[0:26] + "..."
        return self.title

    @property
    def little_description(self):
        if len(self.description) > 20:
            return self.description[0:30] + "..."
        return self.description

    @classmethod
    def create_task(cls, title, description, user_id):
        new_task = Task(title=title, description=description, user_id=user_id)
        db.session.add(new_task)
        db.session.commit()

        return new_task

    @classmethod
    def get_by_id(cls, id):
        return Task.query.filter_by(id=id).first()

    @classmethod
    def update_task(cls, id, title, description):
        task = Task.get_by_id(id)

        if task is None:
            return False

        task.title = title
        task.description = description

        db.session.add(task)
        db.session.commit()

        return task

    @classmethod
    def delete_task(cls, id):
        task = Task.get_by_id(id)

        if task is None:
            return False

        db.session.delete(task)
        db.session.commit()

        return True


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=True)
    email = db.Column(db.String(50), unique=True, nullable=True)
    password_hash = db.Column(db.String(80), nullable=True)
    tasks = db.relationship("Task")

    def __str__(self):
        return f"Id:{self.id}, username:{self.username}, email:{self.email}, password_hash:{self.password_hash}"

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def password(self):
        pass

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value, method="sha256")

    @classmethod
    def create_user(cls, username, email, password_hash):
        new_user = User(username=username, email=email, password=password_hash)
        db.session.add(new_user)
        db.session.commit()

        return new_user

    @classmethod
    def get_by_username(cls, username):
        return User.query.filter_by(username=username).first()

    @classmethod
    def get_by_email(cls, email):
        return User.query.filter_by(email=email).first()

    @classmethod
    def get_by_id(cls, id):
        return User.query.filter_by(id=id).first()
