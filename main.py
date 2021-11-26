import logging
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html", title="HOME PAGE")

@app.route("/docs")
def docs():
    return render_template("docs.html", title="docs page")

@app.route("/about")
def about():
    return render_template("about.html", title="about page")



if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080,debug=True)