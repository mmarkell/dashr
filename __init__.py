from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/dasher.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Miranda\Desktop\\dasher.db'

db = SQLAlchemy(app)

import dasher.views
import dasher.models
