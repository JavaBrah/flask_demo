# We import the `Flask` and `jsonify` classes from the Flask library.
from models import *
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass


# We create a Flask application by initializing the `app` object.
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg://kegan:linux@localhost/bd_example"
db.init_app(app)
# db = SQLAlchemy(app)
# Sample student data
students = [
     {'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
     {'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
     {'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
     {'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
     {'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
     {'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
     {'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
     {'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
     {'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
     {'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
 ]

"""
-Views are bulit to receive requests and generate responses
-Route is a set url pattern that will route a request to the correct view
"""


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
