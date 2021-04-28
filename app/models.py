from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=True)
    description = db.Column(db.String(240), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __str__(self):
        return f"Id:{self.id}, title:{self.title}, description:{self.description}, user_id:{self.user_id}"

    @property
    def little_title(self):
        """Make more small the title because in the dashboard, that looks bad

        Returns:
            string: the title but more small
        """

        if len(self.title) > 38:
            return self.title[0:38] + "..."
        return self.title

    @property
    def little_description(self):
        if len(self.description) > 50:
            return self.description[0:40] + "..."
        return self.description

    @classmethod
    def create_task(cls, title, description, user_id):
        """Create a object type task and insert in the database

        Args:
            title (string): Task's title
            description (string): Task's description
            user_id (int): It's the id of the user to which the task belongs

        Returns:
            objetc tasks: It's the task who has title, description and user_id
        """

        new_task = Task(title=title, description=description, user_id=user_id)
        db.session.add(new_task)
        db.session.commit()

        return new_task

    @classmethod
    def get_by_id(cls, id):
        """Get the object user by id

        Args:
            id (int): the task's id

        Returns:
            object task: return the object task who was finded
        """
        return Task.query.filter_by(id=id).first()

    @classmethod
    def update_task(cls, id, title, description):
        task = Task.get_by_id(id)
        """Update the task

        Returns:
            object task: return the object task but with the propierties changed
        """

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
        """delte one task by id

        Returns:
            boolean: return true if the task was removed successfully and false if the task was removed unccessfully
        """

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
        """verify if the password is correct or not

        Args:
            password (string): string with hash

        Returns:
            boolean: it's true if the password is corresponds to the user
        """
        return check_password_hash(self.password_hash, password)

    @property
    def password(self):
        pass

    @password.setter
    def password(self, value):
        """help to hash the password who is give by the client

        Args:
            value (string): password but hashed
        """
        self.password_hash = generate_password_hash(value, method="sha256")

    @classmethod
    def create_user(cls, username, email, password_hash):
        """create one object user

        Args:
            username (string): user's username
            email (string): user's email
            password_hash (string): user's password with hash

        Returns:
            object user: return the user created
        """
        new_user = User(username=username, email=email, password=password_hash)
        db.session.add(new_user)
        db.session.commit()

        return new_user

    @classmethod
    def get_by_username(cls, username):
        """get the object user by username

        Args:
            username (string): username was gived by the client

        Returns:
            object user: return the object user was finded by de username
        """
        return User.query.filter_by(username=username).first()

    @classmethod
    def get_by_email(cls, email):
        """get the object user by id

        Args:
            email (string): string who was give by the client

        Returns:
            object user: return the object user who was finded by the email
        """
        return User.query.filter_by(email=email).first()

    @classmethod
    def get_by_id(cls, id):
        """Get the object user by id

        Args:
            id (int): id who was gived by the client

        Returns:
            object user: return the object finded by id
        """
        return User.query.filter_by(id=id).first()
