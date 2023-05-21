from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

#create an instance of Flas
app = Flask(__name__)

#create an api object
api = Api(app)

#configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emp.db'

#changed in version 3.0 - disabled by default 
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#sqlalchemy ORM - initialize extension 
db = SQLAlchemy(app)

#context 
app.app_context().push()

#@app.route('/')
#def hello():
#    return "Hello!"

#add a class model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(80), nullable=False)
    salary = db.Column(db.Float)

    def __repr__(self):
        return f"{self.firstname} {self.lastname} - {self.gender} - {self.salary}"
    
