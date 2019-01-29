from flask import Flask

lexus = Flask(__name__)

@app.route("/")
def home():
    return "Hello Ladies"