import os
from dotenv import load_dotenv

load_dotenv()


class Test:
    SECRET_KEY = os.getenv("SECRET_KEY")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://root:{MYSQL_PASSWORD}@localhost/test"

class Test1:
    SECRET_KEY1 = os.getenv("SECRET_KEY1")

config = {
    "test" : Test,
    "test1" : Test1
}
