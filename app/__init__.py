from flask import Flask
from config import Config
from flask_pymongo import PyMongo

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

from app import routes, errors
