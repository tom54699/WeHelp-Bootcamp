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
                check = "select*from member where account = %s;"
                cursor.execute(check,(regi_account,))
    
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
    check = "select*from member where account = %s;"
    cursor.execute(check,(account,))

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
            "message_id": i[1],
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
        # 傳送實際id 未來要刪除可能比較好做
        data.update({f"{i[1]}":f"{i[0]}: {i[3]}"})
    return jsonify(data)

@app.route("/deleteAll",methods=["DELETE"])
def deleteAll():
    # 有兩種方式
    delete = "TRUNCATE TABLE message;"  #這種會把資料全部清空,id也歸零
    # delete = "TRUNCATE TABLE message;"
    cursor.execute(delete)
    mydb.commit()
    return jsonify({"status":"成功清除"})

# week-7 查詢會員資料api
error_message = {
    "data":"null"
}

@app.route("/api/member",methods=["GET"])
def member_name_query():
    try:
        if "name" in session:
            account  = request.args.get("account")
            name_query_sql = "SELECT*FROM member WHERE account = %s;"
            cursor.execute(name_query_sql,(account,))
            name_result = cursor.fetchone()
            print("fetch姓名資料結果",name_result)
            if name_result != None:
                id = name_result[0]
                name = name_result[1]
                account = name_result[2]
                name_response = {
                    "data":{
                        "id":id,
                        "name":name,
                        "account":account
                    }
                }
                return jsonify(name_response)
            else:
                return jsonify(error_message)
        else:
            return jsonify(error_message)
    except Exception as ex:
        print(ex)
        return jsonify(error_message)
@app.route("/api/member",methods=["PATCH"])

def update_name():
    try:
        if "name" in session:
            name = session["name"]
            request_name  = request.json.get("name")
            name_query_sql = "UPDATE member SET name=%s WHERE name=%s;"
            cursor.execute(name_query_sql,(request_name,name,))
            mydb.commit()
            print("更新狀態",cursor.rowcount)
            if cursor.rowcount > 0:
                session["name"] = request_name
                return jsonify(ok = "true")
            else:
                return jsonify(error = "true")
        else:
            return jsonify(error_message)
    except Exception as ex:
        print(ex)
        return jsonify(error = "true")




if __name__ == "__main__":
    app.run(port="3000",debug=True)

#check = f"select*from member where id = '{id}';"
#cursor.execute(check)
#if cursor.rowcount == 0: