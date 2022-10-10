from flask import Flask,request,render_template,redirect,session,url_for

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
    if "account" in session:
        account = session["account"]
        print(session) 
        return render_template("member.html",account=account)
    else:
        return redirect("/")

@app.route("/signin",methods=["POST"])
def signin():
    account = request.form.get("account")
    password = request.form.get("password")
    if account == "" or password == "":
        return redirect("/error?error=請輸入帳號、密碼")
    if account != "test" or password != "test":
        return redirect("/error?error=帳號、或密碼輸入錯誤")
    session["account"] = account
    session["password"] = password
    return  redirect("/member")

@app.route("/error",methods=["GET"])
def err():
    error=request.args.get("error","發生不明錯誤，核彈啟動中")
    return render_template("error.html",error=error)

@app.route("/signout",methods=["GET"])
def signout():
    del session["account"]
    del session["password"]
    # session.clear() 也可以
    return redirect("/")

@app.route("/squareCount",methods=["POST"])  
def squareCount():
    squareNumber = request.form.get("squareNumber")
    print(squareNumber)
    if squareNumber == "":
        return redirect("/error?error=請輸入數字")
    squareNumber = int(squareNumber)
    squareNumber = squareNumber**2
    return redirect(url_for("square",number=squareNumber))

@app.route("/square/<number>")  # 這邊css要改路徑
def square(number):
        return render_template("square.html",number=str(number))


if __name__ == "__main__":
    app.run(port="3000",debug=True)