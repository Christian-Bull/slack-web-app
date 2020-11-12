from flask import Flask
from config import Config
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap

# get static folder
app = Flask(__name__, static_url_path='/static')

# config stuff
app.config.from_object(Config)

# mongodb setup
app.config["MONGO_URI"] = "mongodb://localhost/slack"
mongo = PyMongo(app)

# setup bootstrap
bootstrap = Bootstrap(app)

# errors
from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

# from redis import Redis
# import rq

# # redis tasks
# app.redis = Redis.from_url(app.config['REDIS_URL'])
# app.task_queue = rq.Queue('slack-web-tasks', connection=app.redis)


from app import routes, errors
