import functools
from flask import Flask, render_template, flash

app = Flask(__name__)
app.secret_key = "jose"


@app.route("/")
def home():
    flash("This is a flashed message.")
    flash("Another message.")
    return render_template("home.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")