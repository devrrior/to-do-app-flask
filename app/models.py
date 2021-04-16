from app import db
from werkzeug.security import check_password_hash, generate_password_hash

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40),nullable=True)
    body = db.Column(db.String(140),nullable=True)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    user = db.relationship("User",backref=db.backref("tasks",lazy=True))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=True)
    email = db.Column(db.String(50),unique=True,nullable=True)
    password_hash = db.Column(db.String(80),nullable=True)

    @property
    def password(self):
        pass

    @password.setter
    def password(self,value):
        self.password_hash = generate_password_hash(value,method="sha256")

    @classmethod
    def create_user(cls,username,email,password_hash):
       new_user = User(username=username,email=email,password=password_hash)
       db.session.add(new_user)
       db.session.commit()

       return new_user

    @classmethod
    def get_by_username(cls,username):
       return User.query.filter_by(username=username).first()

    @classmethod
    def get_by_email(cls,email):
       return User.query.filter_by(email=email).first()

