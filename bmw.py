from flask import Flask, render_template

lexus = Flask(__name__)

@lexus.route("/")
def home():
    return render_template("index.html")