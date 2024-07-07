#!/usr/bin/env python3

from models import db, Scientist, Mission, Planet
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask import Flask, make_response, jsonify, request
import os

# Base directory and database configuration
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

# Flask application setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Database and migration initialization
db.init_app(app)
migrate = Migrate(app, db)

# Flask-RESTful API initialization
api = Api(app)

@app.route('/')
def home():
    return 'Welcome to the API'

class Scientists(Resource):
    def get(self):
        try:
            scientists = Scientist.query.all()
            new_scientists = [s.to_dict(only=("id", "name", "field_of_study")) for s in scientists]
            return new_scientists, 200
        except Exception as e:
            return {"error": str(e)}, 400

class ScientistById(Resource):
    def get(self, id):
        try:
            scientist = Scientist.query.filter_by(id=id).first()
            if scientist:
                return scientist.to_dict(), 200
            else:
                return {"error": "Scientist not found"}, 404
        except Exception as e:
            return {"error": str(e)}, 400

# Adding resources to the API
api.add_resource(Scientists, "/scientists")
api.add_resource(ScientistById, "/scientists/<int:id>")

if __name__ == '__main__':
    app.run(port=5555, debug=True)
