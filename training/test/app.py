from flask import Flask,request,render_template

import json

from requests import session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/count",methods=["POST"])
def count():
    num = request.json["num"]
    num = int(num)
    num = num**2
    return {"num":num}


if __name__ == "__main__":
    app.run(debug=True)