from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


# def length_honeypot(form, field):
#         if len(field.data) > 0:
#                 raise validators.ValidationError("Area must be empty")

class SignupForm(FlaskForm):
    email = StringField("Email",validators=[
        DataRequired(),
        Email()
    ])
    username = StringField("Username",validators=[
        Length(max=30,min=4),
        DataRequired()
    ])
    password= PasswordField("Password",validators=[
        DataRequired()
    ])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    username = StringField("Username",validators=[
        DataRequired(),
    ])
    password= PasswordField("Password",validators=[
        DataRequired()
    ])
    submit = SubmitField("Submit")
