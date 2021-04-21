from app import db, login_manager
from app.form import LoginForm, SignupForm
from app.models import User
from flask import Blueprint, redirect, render_template, request, url_for, flash, session
from flask_login import login_user, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash


@login_manager.user_loader
def load_user(id):
    return User.get_by_id(id)


auth_bp = Blueprint(
    "auth_bp", __name__, template_folder="templates", static_folder="static"
)


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    signup_form = SignupForm()

    if current_user.is_authenticated:
        return redirect(url_for("tasks_bp.tasks"))

    if signup_form.validate_on_submit():
        user = User.create_user(
            signup_form.username.data, signup_form.email.data, signup_form.password.data
        )
        flash(f"Account created for {signup_form.username.data}", "success")
        login_user(user)
        return redirect(url_for("tasks_bp.tasks"))

    return render_template("auth/signup.html", title_page="Sign Up", form=signup_form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()

    if current_user.is_authenticated:
        return redirect(url_for("tasks_bp.tasks"))

    if login_form.validate_on_submit():
        user = User.query.filter(User.username == login_form.username.data).first()

        if user and user.verify_password(login_form.password.data):
            flash("You have been logged in!", "success")
            login_user(user)
            return redirect(url_for("tasks_bp.tasks"))
        flash("Login unsuccesful. Please check username and password.", "danger")
        return redirect(url_for("auth_bp.login"))

    return render_template("auth/login.html", title_page="Login", form=login_form)


@auth_bp.route("/logout")
def logout():
    logout_user()
    flash("Logout successful!", "success")
    return redirect(url_for("auth_bp.login"))
