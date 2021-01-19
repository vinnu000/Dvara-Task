from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config["SECRET_KEY"] = "secret_key"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:password@localhost/flaskapp'

db = SQLAlchemy(app)
