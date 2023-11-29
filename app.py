import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/template1")
def template1():
    return render_template("template1.html")

@app.route("/template2")
def template2():
    return render_template("template2.html")


@app.route("/template3")
def template3():
    return render_template("template3.html")


@app.route("/template4")
def template4():
    return render_template("template4.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)