from flask import Flask
from flask_cors import CORS
from psycopg2 import connect

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# db_connection = connect()
from api import dashboard