# partially based off of https://realpython.com/blog/python/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)


from models import *

@app.route('/')
def index():
	return 'index page!'

@app.route('/home')
def home():
	return 'home page!'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')