from app import app
from flask import render_template

@app.route("/")
def index():
    title_page = "Home"
    username = "Fernando"
    return render_template("index.html",title_page=title_page,username=username)
