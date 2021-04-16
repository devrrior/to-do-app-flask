from app import db
from app.form import LoginForm, SignupForm
from app.models import User
from flask import Blueprint, redirect, render_template, request, url_for, flash, session
from werkzeug.security import check_password_hash, generate_password_hash

auth = Blueprint("auth", __name__,
    template_folder="templates",
    static_folder="static", static_url_path="assets")

@auth.route("/signup", methods=["GET","POST"])
def signup():
    signup_form = SignupForm()
    title_page = "Sign Up"

    if signup_form.validate_on_submit():
        User.create_user(signup_form.username.data, signup_form.email.data, signup_form.password.data)
        flash(f"Account created for {signup_form.username.data}","success")
        return redirect(url_for("auth.login"))

    return render_template("auth/signup.html",title_page=title_page,form=signup_form)

@auth.route("/login",methods=["GET","POST"])
def login():
    login_form = LoginForm()
    title_page = "Login"

    if login_form.validate_on_submit():
        user = User.query.filter(User.username == login_form.username.data).first()

        if user and check_password_hash(user.password_hash,login_form.password.data):
            flash("You have been logged in!","success")
            session["username"] = login_form.username.data
            return redirect(url_for('general.index'))
        flash("Login unsuccesful. Please check username and password.","danger")
        return redirect(url_for("auth.login"))

    return render_template("auth/login.html",title_page=title_page,form=login_form)
