from flask import Blueprint, render_template, redirect, url_for

general_bp = Blueprint(
    "general_bp", __name__, template_folder="templates", static_folder="static"
)


@general_bp.route("/")
def index():
    title_page = "Home"
    username = "Fernando"
    # return render_template("general/index.html",title_page=title_page,username=username)
    return redirect(url_for("auth_bp.login"))