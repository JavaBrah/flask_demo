# We import the `Flask` and `jsonify` classes from the Flask library.
from models import *
from flask import Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy
# Don't need this import, check models.py
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass


# We create a Flask application by initializing the `app` object.
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg://kegan:linux@localhost/bd_example"
#Imported db from models.py
db.init_app(app)
# db = SQLAlchemy(app)
# Sample student data



@app.route("/api/v1/staff/", methods=['GET'])
def show_staff():
    return get_staff()







@app.route("/")
def home():
    return "<h1>Hey there</h1>"

if __name__ == '__main__':
    with app.app_context():
         post_students(students)

    app.run(debug=True, port=8000)
    

    # Flask tries to run on port 5000 by default but it's sometimes
    # occupied by a different function. Let's tell flask to utilize port 8000 instead
