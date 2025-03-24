from flask import Flask
from flask_cors import CORS
from routes import routes
from models import db
from utils import EnvVars, ErrorMessages
from adaptors import DBAdaptor

# Initiate a Flask application.
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": [
    "http://localhost:3000",
    "https://www.shahtech.info"
    ]}})

db.config_app(app)

# Register the blueprint of all the routes.
# API calls for the assigned url prefix will be redirected to the routes.
app.register_blueprint(routes, url_prefix="/")