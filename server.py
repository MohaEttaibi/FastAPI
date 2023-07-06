from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/greet")
@app.route("/greet/<name>")
def greet(name=None):
    return render_template("greet.html", name=name)
