from flask import render_template
from app import app

@app.route("/signup")
def register():
    title_page = "Sign Up"
    return render_template("signup.html",title_page=title_page) 