from flask import Flask , render_template , jsonify
import random

app = Flask(__name__)

@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/przyczyna1")
def przyczyna1():
    return render_template("przyczyna1.html")

@app.route("/rozwiązanie1")
def rozwiązanie1():
    return render_template("rozwiązanie1.html")

@app.route("/przyczyna2")
def przyczyna2():
    return render_template("przyczyna1.htm2")

@app.route("/rozwiązanie2")
def rozwiązanie2():
    return render_template("rozwiązanie2.html")

@app.route("/twójpomysł")
def twójpomysł():
    return render_template("twójpomysł.html")