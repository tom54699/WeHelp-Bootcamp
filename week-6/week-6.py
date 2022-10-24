from flask import Flask,request,render_template,redirect,session,url_for,jsonify
import mysql.connector
import os
from flask_bcrypt import Bcrypt
from setting import BaseConfig
from flask_cors import CORS

app=Flask(__name__)
app.config.from_object(BaseConfig)

CORS(app)
bcrypt=Bcrypt(app)

mydb = mysql.connector.connect(
    host = "localhost",
    database = "website",
    user = "root",
    password = BaseConfig.DB_PASSWORD,
    charset = "utf-8"
)
cursor = mydb.cursor(buffered=True)

@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/member",methods=["GET"])
def member():
    if "name" in session:
        name = session["name"]
        return render_template("member.html",name = name)
    else:
        return redirect("/")

@app.route("/signup",methods=["POST"])
def signup():
        try:
            if request.method == "POST":
                # 拿使用者輸入的資料
                regi_name = request.form["regi_name"]
                regi_account = request.form["regi_account"]
                regi_password = request.form["regi_password"]
                print(regi_name,regi_account,regi_password)
                # 確認account有無重複
                check = f"select*from member where account = '{regi_account}';"
                cursor.execute(check)
    
                if cursor.rowcount != 0:
                    return redirect("/error?error=帳號已被註冊")
                else:
                    pw_hash = bcrypt.generate_password_hash(regi_password, 10) 
                    print(type(pw_hash))  
                    insert = "INSERT INTO member(name,account,password)VALUES(%s,%s,%s)"
                    cursor.execute(insert,(regi_name,regi_account,pw_hash))
                    mydb.commit()
                    return redirect("/")
        except Exception as ex:
            return redirect(f"/error?error='錯誤訊息:{ex}'") 


@app.route("/signin",methods=["POST"])
def signin():
    account = request.form.get("account")
    password = request.form.get("password")

    if account == "" or password == "":
        return redirect("/error?error=請輸入帳號、密碼")
    check = f"select*from member where account = '{account}';"
    cursor.execute(check)

    if cursor.rowcount == 0:
        return redirect("/error?error=此帳號沒有註冊")
    for data in cursor:
        print("篩選結果:",data)
    id = data[0]
    name = data[1]
    account1 = data[2]
    password1 = data[3]
    if bcrypt.check_password_hash(password1,password):
        session["account"] = account1
        session["name"] = name
        session["id"] = id
        return redirect("/member")
    else:
        return redirect("/error?error=密碼輸入錯誤")


@app.route("/error",methods=["GET"])
def err():
    error=request.args.get("error","發生不明錯誤，核彈啟動中")
    return render_template("error.html",error=error)

@app.route("/signout",methods=["GET"])
def signout():
    del session["account"]
    del session["name"]
    # session.clear() 也可以
    return redirect("/")

@app.route("/message",methods=["POST"])
def sendmessage():
    id = session["id"]
    print(session)
 
    content = request.json
    
    content = content["content"]
    insert = "INSERT INTO message(member_id,content)VALUES(%s,%s)"
    cursor.execute(insert,(id,content))
    mydb.commit()
    
    # 文章編號
    check = "select member.name,message.id,message.member_id,message.content,message.time from member inner join message on member.id = message.member_id where content = %s and member_id = %s;"
    cursor.execute(check, (content,id))
    if cursor.rowcount == 0:
        return redirect("/error?error=資料庫找不到文章")
    for i in cursor:
        data = {
            "content": content,
            "message_id": i[2],
            "name": i[0],
            "time":i[4]
        }
    return jsonify(data)

@app.route("/getMessage")
def getMessage():
    id = session["id"]
    print(session)
    
    check = "select member.name,message.id,message.member_id,message.content from member inner join message on member.id = message.member_id;"
    cursor.execute(check)
    if cursor.rowcount == 0:
        return redirect("/error?error=資料庫找不到文章")
    data = {}
    for i in cursor:
        data.update({f"message{i[1]}":f"{i[0]}: {i[3]}"})
    return jsonify(data)


if __name__ == "__main__":
    app.run(port="3000",debug=True)

#check = f"select*from member where id = '{id}';"
#cursor.execute(check)
#if cursor.rowcount == 0: