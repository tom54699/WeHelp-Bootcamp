from flask import Flask, make_response,request,render_template,redirect,session,url_for
from requests import delete

app=Flask(__name__)
app.config['SECRET_KEY'] = b'\xeb\xe3\xceF\xf6\xa1u\t&\x95\xf8\xefPK\xc7\xa8'

account={
    "account":"test",
    "password":"test"
}


@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/member",methods=["GET"])
def member():
    """
    if "account" in session:
        account = session["account"]
        print(session) 
        return render_template("member.html",account=account)
    else:
        return redirect("/")
    """
    if "account" in request.cookies:
        account = request.cookies.get("account")
        print(account) 
        return render_template("member.html",account=account)
    else:
        print("沒有驗證!")
        return redirect("/")

@app.route("/signin",methods=["POST"])
def signin():
    account = request.form.get("account")
    password = request.form.get("password")
    if account == "" or password == "":
        return redirect("/error?error=請輸入帳號、密碼")
    if account != "test" or password != "test":
        return redirect("/error?error=帳號、或密碼輸入錯誤")
    #session["account"] = account
    #session["password"] = password
    resp = make_response(redirect("/member"))
    resp.set_cookie(key="account",value="test")
    return  resp

@app.route("/error",methods=["GET"])
def err():
    error=request.args.get("error","發生不明錯誤，核彈啟動中")
    return render_template("error.html",error=error)

@app.route("/signout",methods=["GET"])
def signout():
    #del session["account"]
    #del session["password"]
    # session.clear() 也可以
    res = make_response(redirect("/"))
    res.delete_cookie("account")
    return res


"""
@app.route("/squareCount",methods=["POST"])  
def squareCount():
    squareNumber = request.form.get("squareNumber")
    print(squareNumber)
    if squareNumber == "":
        return redirect("/error?error=請輸入數字")
    squareNumber = int(squareNumber)
    squareNumber = squareNumber**2
    return redirect(url_for("square",number=squareNumber))
"""

@app.route("/square/<number>") 
def square(number):
    number = int(number)
    number = number**2
    return render_template("square.html",number=str(number))


if __name__ == "__main__":
    app.run(port="3000",debug=True)