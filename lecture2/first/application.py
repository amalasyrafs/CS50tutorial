from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!!!!!!!!!"

@app.route("/amal")
def david():
    return "Hello Amal!!!!"