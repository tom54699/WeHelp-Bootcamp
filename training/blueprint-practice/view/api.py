from flask import Blueprint, Flask

app2 = Blueprint("app2", __name__)

@app2.route("/app2/<a>")
def show(a):
    print(a)
    return 'pages/app2 {}'.format(a)
