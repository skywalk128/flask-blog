from flask import Flask
from flask.ext.mongoengine import MongoEngine
import datetime

app = Flask(__name__)
app.config.from_object("config")
app.config['SECRET_KEY'] = str(datetime.datetime)

db = MongoEngine(app)

from app import views, models