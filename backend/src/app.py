from flask import Flask
from flask_cors import CORS
from routes import routes
from models import db
from seeds import seed_all_tables

# Initiate a Flask application.
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": [
    "http://localhost:3000",
    "https://www.shahtech.info"
    ]}})

db.config_app(app)

db.add_sample_data(app, seed_all_tables)

# Register the blueprint of all the routes.
# API calls for the assigned url prefix will be redirected to the routes.
app.register_blueprint(routes, url_prefix="/")