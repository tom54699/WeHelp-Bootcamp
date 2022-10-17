from flask import Flask,Blueprint,url_for
from view.api import app2

app = Flask(__name__)

@app.route("/")
def index():
    test = url_for("app2.show",a=50)
    return test

app.register_blueprint(app2,url_prefix='/pages')

if __name__ == "__main__":
    app.run(debug=True)