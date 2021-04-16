from app import db

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
    password = db.Column(db.String(80),nullable=True)