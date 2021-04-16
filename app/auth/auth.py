from app import db
from app.form import LoginForm, SignupForm
from app.models import User
from flask import Blueprint, redirect, render_template, request, url_for
from werkzeug.security import check_password_hash, generate_password_hash

auth = Blueprint("auth", __name__,
    template_folder="templates",
    static_folder="static", static_url_path="assets")

@auth.route("/signup", methods=["GET","POST"])
def signup():
    signup_form = SignupForm()
    title_page = "Sign Up"

    if signup_form.validate_on_submit():
       password_hash = generate_password_hash(signup_form.password.data, method="sha256")
       new_user = User(username=signup_form.username.data,email=signup_form.email.data,password=password_hash)
       db.session.add(new_user)
       db.session.commit()
       return redirect(url_for("login"))

    return render_template("auth/signup.html",title_page=title_page,form=signup_form)

@auth.route("/login",methods=["GET","POST"])
def login():
    login_form = LoginForm()
    title_page = "Login"

    if login_form.validate_on_submit():
        user = User.query.filter(User.username == login_form.username.data).first()

        if user and check_password_hash(user.password,login_form.password.data):
            return "You're logged!"
        return 'error, tus credenciales no son validas'

    return render_template("auth/login.html",title_page=title_page,form=login_form)
