# We import the `Flask` and `jsonify` classes from the Flask library.
from models import *
from flask import Flask, jsonify, request, render_template
import requests
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

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/api/v1/staff/", methods=['GET'])
def show_staff():
    return get_staff()

if __name__ == '__main__':
    app.run(debug=True, port=8000)


# @app.route('/submit_data', methods=['POST'])
# def submit_data():
#     pokemon_data = None
#     if request.method == 'POST':
#         first_name = request.form.get('first_name')
#         last_name = request.form.get('last_name')
#         pokemon_name = request.form.get('pokeSearch').strip().lower()
#         response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
#         if response.status_code != 200:
#             return jsonify({'success': False, 'error': f"Pokémon '{pokemon_name}' not found."})
       
#         post_people_searching_pokemon(first_name, last_name)
#         data = response.json()
#         pokemon_data = {
#             'name': data['name'].capitalize(),
#             'type_one': data['types'][0]['type']['name'],
#             'type_two': data['types'][1]['type']['name'] if len(data['types']) > 1 else None,
#         }
#         post_searched_pokemon(**pokemon_data)

#         return jsonify({'success': True, 'pokemon': pokemon_data})




    # Flask tries to run on port 5000 by default but it's sometimes
    # occupied by a different function. Let's tell flask to utilize port 8000 instead
