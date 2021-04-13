from flask import render_template
from app import app

@app.route("/login")
def login():
    title_page = "Login"
    return render_template("login.html",title_page=title_page)