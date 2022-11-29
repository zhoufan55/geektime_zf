from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# mysql+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config[
    "SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@42.192.248.147:3306/geektime_0?charset=utf8mb4"
app.secret_key = '404zf'
app.config["JWT_SECRET_KEY"] = "404zf"  # Change this!

app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]
# app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_COOKIE_SECURE"] = False
jwt = JWTManager(app)
CORS(app)
