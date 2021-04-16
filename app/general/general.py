from flask import Blueprint, render_template

general = Blueprint("general", __name__,
    template_folder="templates",
    static_folder="static", static_url_path="assets")

@general.route("/")
def index():
    title_page = "Home"
    username = "Fernando"
    return render_template("general/index.html",title_page=title_page,username=username)
