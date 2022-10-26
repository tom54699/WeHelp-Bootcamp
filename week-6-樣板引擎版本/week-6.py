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
    pool_name='mypool',
    pool_size=10,
    host = "localhost",
    database = "website",
    user = "root",
    password = BaseConfig.DB_PASSWORD,
    charset = "utf-8"
)
#cursor = mydb.cursor(buffered=True)

@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/member",methods=["GET"])
def member():
    try:
        db1 = mysql.connector.connect(pool_name = "mypool")
        cursor = db1.cursor(buffered=True)
        if "name" in session:
            name = session["name"]
            id = session["id"]
            check = "select member.name,message.id,message.member_id,message.content from member inner join message on member.id = message.member_id;"
            cursor.execute(check)
            data = ""
            for i in cursor:
                # 傳送實際id 未來要刪除可能比較好做
                data = data + f"{i[0]}:{i[3]}"+"<br/>"
            print(data)

            return render_template("member.html",name = name, messages = data)
        else:
            return redirect("/")
    except Exception as ex:
        return redirect(f"/error?error='錯誤訊息:{ex}'") 
    finally:
        db1.close()  

@app.route("/signup",methods=["POST"])
def signup():
        try:
            db2 = mysql.connector.connect(pool_name = "mypool")
            cursor = db2.cursor(buffered=True)
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
                    db2.commit()
                    return redirect("/")
        except Exception as ex:
            return redirect(f"/error?error='錯誤訊息:{ex}'") 
        finally:
            db2.close()  

@app.route("/signin",methods=["POST"])
def signin():
    try:
        db3 = mysql.connector.connect(pool_name = "mypool")
        cursor = db3.cursor(buffered=True)
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
    except Exception as ex:
        return redirect(f"/error?error='錯誤訊息:{ex}'") 
    finally:
        db3.close()  

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

@app.route("/message/<content>")
def sendmessage(content):
    try:
        db4 = mysql.connector.connect(pool_name = "mypool")
        cursor = db4.cursor(buffered=True)
        id = session["id"]
        print(content)

        insert = "INSERT INTO message(member_id,content)VALUES(%s,%s)"
        cursor.execute(insert,(id,content))
        db4.commit()
        
        # 文章編號
        check = "select member.name,message.id,message.member_id,message.content,message.time from member inner join message on member.id = message.member_id where content = %s and member_id = %s;"
        cursor.execute(check, (content,id))

        return redirect("/member")
    except Exception as ex:
        return redirect(f"/error?error='錯誤訊息:{ex}'") 
    finally:
        db4.close()  


@app.route("/deleteAll",methods=["DELETE"])
def deleteAll():
    try:
        db5 = mysql.connector.connect(pool_name = "mypool")
        cursor = db5.cursor(buffered=True)
        # 有兩種方式
        delete = "TRUNCATE TABLE message;"  #這種會把資料全部清空,id也歸零
        # delete = "TRUNCATE TABLE message;"
        cursor.execute(delete)
        db5.commit()
        return jsonify({"status":"成功清除"})
    except Exception as ex:
        return redirect(f"/error?error='錯誤訊息:{ex}'") 
    finally:
        db5.close()  

if __name__ == "__main__":
    app.run(port="3000",debug=True)

#check = f"select*from member where id = '{id}';"
#cursor.execute(check)
#if cursor.rowcount == 0: