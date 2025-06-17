# We import the `Flask` and `jsonify` classes from the Flask library.
from flask import Flask, jsonify

# We create a Flask application by initializing the `app` object.
app = Flask(__name__)

# Sample student data
students = [
     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
     {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
     {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
     {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
     {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
     {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
     {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
     {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
 ]

"""
-Views are bulit to receive requests and generate responses
-Route is a set url pattern that will route a request to the correct view
"""


# We define a route `/students` that responds to GET requests.
@app.route('/api/v1/students/', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/api/v1/old_students/', methods=['GET'])
def get_old_students():
    lst = []
    for s in students:
        if s['age'] > 20:
            lst.append(s)
    return jsonify(lst)

@app.route('/api/v1/advance_students/', methods=['GET'])
def get_advanced_students():
    lst = [x for x in students if x['age'] < 21 and x['grade'] == "A"]
    return jsonify(lst)

@app.route('/api/v1/student_names/', methods=['GET'])
def get_student_names():
    lst =[]
    for s in students:
        dic = {
            "first_name": s['first_name'],
            "last_name": s['last_name'],                
            'age': s['age']
        }
        lst.append(dic)
    # lst = [f"first_name: {x['first_name']} last_name: {x['last_name']} age: {x["age"]}" for x in students]
    return jsonify(lst)

@app.route('/api/v1/student_ages/', methods=['GET'])
def get_student_ages():
    lst =[]
    for s in students:
        dic = {
            "first_name": s['first_name'],
            "last_name": s['last_name'],
            'age': s['age']
        }
        lst.append(dic)
    # lst = [f"first_name: {x['first_name']} last_name: {x['last_name']} age: {x["age"]}" for x in students]
    return jsonify(lst)



@app.route("/")
def home():
    return "<h1>Hey there</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=8000) 
    # Flask tries to run on port 5000 by default but it's sometimes
    # occupied by a different function. Let's tell flask to utilize port 8000 instead
