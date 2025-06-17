from flask import jsonify
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))


class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    year_employed = db.Column(db.String(20))

def post_students(students: list):
    for s in students:
        student = Students(
                first_name= s['first_name'],
                last_name= s['last_name'],
                age= s['age'],
                grade= s['grade'],
        )
        db.session.add(student)
    db.session.commit()


def get_students():
    students = Students.query.all()
    formatted_students = []
    for s in students:
        formatted_students.append(
            {
                "id": s.id,
                "first_name": s.first_name,
                "last_name": s.last_name,
                "age": s.age,
                "grade": s.grade,
            }
        )
    return jsonify(formatted_students)

def get_staff():
    staff_list = []
    staff = Staff.query.all()
    for s in staff:
        staff_list.append(
            {
                "id": s.id,
                "first_name": s.first_name,
                "last_name": s.last_name,
                "age": s.age,
                "year_employed": s.year_employed,
            }
        )
    return jsonify(staff_list)

# def get_advanced_students():
#     lst = [x for x in students if x['age'] < 21 and x['grade'] == "A"]
#     return jsonify(lst)

# def get_student_names():
#     lst =[]
#     for s in students:
#         dic = {
#             "first_name": s['first_name'],
#             "last_name": s['last_name'],                
#             'age': s['age']
#         }
#         lst.append(dic)
    
#     return jsonify(lst)


# def get_student_ages():
#     lst =[]
#     for s in students:
#         dic = {
#             "first_name": s['first_name'],
#             "last_name": s['last_name'],
#             'age': s['age']
#         }
#         lst.append(dic)
#     # lst = [f"first_name: {x['first_name']} last_name: {x['last_name']} age: {x["age"]}" for x in students]
#     return jsonify(lst)