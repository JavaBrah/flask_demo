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




@app.route('/submit_data', methods=['POST'])
def submit_data():
    error = None
    pokemon_data = None
    if request.method == 'POST':
        # first_name = request.form['first_name']
        # last_name = request.form['last_name']
        pokemon = request.form['pokeSearch']
        
        pokemon_name = request.form(pokemon).strip().lower()
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")

        if response.status_code == 200:
            data = response.json()
            pokemon_data = {
                'name': data['name'].capitalize(),
                'type_one': data['types'][0]['type']['name'],
                'type_two': data['types'][1]['type']['name'],
                'sprite': data['sprites']['front_default']
            }
            return jsonify({'success': True, 'pokemon': pokemon_data})
        else:
            return jsonify({'success': False, 'error': f"Pokémon '{pokemon_name}' not found."})


@app.route("/api/v1/staff/", methods=['GET'])
def show_staff():
    return get_staff()

@app.route("/")
def home():
    return "<h1>Hey there</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=8000)

    # Flask tries to run on port 5000 by default but it's sometimes
    # occupied by a different function. Let's tell flask to utilize port 8000 instead
