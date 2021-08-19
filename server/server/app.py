from flask import Flask , request , jsonify
from flask_sqlalchemy import SQLAlchemy
import os 

currentDirectory = os.getcwd() 
databasePath = os.path.join(currentDirectory , "database.db")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+databasePath
db = SQLAlchemy(app) 

import routes , models 