from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	headline = "HELLO WORLD!"
	return render_template("index.html", headline=headline)

""" @app.route("/<string:name>")
def hello(name):
	return "Hello, {}".format(name)

@app.route("/ali")
def ali():
	return "Hello, Ali!" """