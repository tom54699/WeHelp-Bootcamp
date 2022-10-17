from typing import Text
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from config import SECRET_KEY
from config import config

db = SQLAlchemy()

app=Flask(__name__)
#app.config.from_pyfile('config.py')
#app.config.from_object(config)
app.config.from_object(config["test"])


db.init_app(app)


class Product(db.Model):
    __tablename__ = "product"
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    db_product_buylist = db.relationship("Buylist", backref="product")

    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def __repr__(self):
        return "(%s, %s)" % (self.name, self.price)

class User(db.Model):
    __tablename__ = "user"
    uid = db.Column(db.Integer, primary_key=True)
    name =db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    db_user_atc = db.relationship("Buylist", backref="user")

    def __init__(self,name,password):
        self.name = name
        self.password = password

class Buylist(db.Model):
    __tablename__ = "buylist"
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(5), nullable=False)

    uid = db.Column(db.Integer, db.ForeignKey("user.uid"), nullable=False)
    pid = db.Column(db.Integer, db.ForeignKey('product.pid'), nullable=False)

    def __init__(self,uid,pid,state):
        self.uid =uid
        self.pid = pid
        self.state = state

@app.route("/")
def index():
    p1 =Product("car",60)
    print(p1) # 有沒有__repr__ 印出的東西有差別
    """
    db.create_all() 

    p1  = Product("Novel",8888)
    p2 = Product("Notebook",88888)
    p3 = Product("Monitor",25000)
    p4 = Product("house",354000000)
    p = [p1,p2,p3,p4]
    db.session.add_all(p)
    u1 = User("Tom",123456)
    u2 = User("Toml",5646)
    u3 = User("Nancy",549864)
    u = [u1,u2,u3]
    db.session.add_all(u)
    atc1 = Buylist(1,4,"Y")
    db.session.add(atc1)
    db.session.commit()
    """
    # query = Product.query.filter_by(name='house').first()
    query = Buylist.query.first()
    print(query.product.name)
    print(query.user.name)
    print(query)
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)

