from flask import Flask
from flask_cors import CORS
from model.db import db
from utils.env_variable import port, postgres_connection_string

# Import all the routes.
from routes import routes

# Initiate a Flask application.
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": [
    "http://localhost:3000",
    "https://www.shahtech.info"
    ]}})

app.config["SQLALCHEMY_DATABASE_URI"] = postgres_connection_string

db.init_app(app)

# Register the blueprint of all the routes.
# API calls for the assigned url prefix will be redirected to the routes.
app.register_blueprint(routes, url_prefix="/")

if __name__ == "__main__":

    if port:
        # Run the application.
        app.run(host="0.0.0.0",debug=True, port=port)