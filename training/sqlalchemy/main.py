from flask_sqlalchemy import SQLAlchemy
from flask import Flask,request
from datetime import datetime

db = SQLAlchemy()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1m2o3o4n@localhost:3306/test2"

db.init_app(app)

relations = db.Table(
    "relations",
    db.Column("product_rt",db.Integer,db.ForeignKey("product.product_id")),
    db.Column("tagid_rt",db.Integer,db.ForeignKey("tag.tagid"))

)

class User(db.Model):
    __tablename__ = "user"
    pid = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(30),unique=True,nullable=False)
    age = db.Column(db.Integer, nullable=False)
    insert_time = db.Column(db.DateTime, default=datetime.now)

    db_user_store = db.relationship("Store",backref="user")

    def __init__(self,name,age,insert_time):
        self.name = name
        self.age = age
        self.insert_time = insert_time

class Store(db.Model):
    __tablename__ = "store"
    sid = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(30),unique=True,nullable=False)
    address = db.Column(db.String(30), nullable=False)

    pid = db.Column(db.Integer, db.ForeignKey("user.pid"), nullable=False)
    
    def __init__(self,name,address,pid):
        self.name = name
        self.address = address
        self.pid =pid
class Product(db.Model):
    __tablename__ = "product"
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),unique=True,nullable=False)

    db_product_tag = db.relationship("Tag", secondary=relations, backref = "product")

    def __init__(self,name):
        self.name = name


class Tag(db.Model):
    __tablename__ = 'tag'
    tagid = db.Column(db.Integer, primary_key=True)
    tag_type = db.Column(db.String(30))

    #db_tag_user = db.relationship("User", secondary=relations,backref="tag")

    def __init__(self, tag_type):
        self.tag_type = tag_type
        

@app.route("/")
def index():
    db.create_all()
    """
    db.create_all()
    user_1 = User("Tom",20,"1999-07-06")
    u1 = User("Tofm",20,"1988-07-06")
    u2 = User("Toml",40,"1980-11-19")
    u3 = User("kok",10,"2099-02-06")
    u4 = User("hdh",26,"1859-06-20")
    u = [u1,u2,u3,u4]
    db.session.add(user_1)
    db.session.add_all(u)
    db.session.commit()
    s1 = Store("火鍋","新竹",1)
    s2 = Store("早餐店","台中",2)
    s = [s1,s2]
    db.session.add_all(s)
    db.session.commit()
    tag1 = Tag('免運費')
    tag2 = Tag('新貨到')

    p1 = Product("遊戲")
    p2 = Product("螢幕")
    p= [p1,p2]

    p1.db_product_tag = [tag1,tag2]
    p2.db_product_tag = [tag2]
    db.session.add_all(p)
    db.session.commit()
    """
    
    data1 = User.query.filter_by(name="Toml").first()
    print(data1)
    data = Store.query.all()
    print(data[1].user.name)
    data3 = Product.query.filter_by(name="遊戲").first()
    print(data3)
    print(data3.name)
    print(data3.db_product_tag)
    data3 = data3.db_product_tag[1].tag_type
    print(data3)


    #db.session.delete(data2)

    return "hi"

if __name__ == "__main__":
    app.run(debug=True)