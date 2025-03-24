from flask import Flask
from flask_cors import CORS
from models import db
from utils import EnvVars, ErrorMessages
from routes import routes

if not EnvVars.POSTGRESQL_CONNECTION_STRING:
    raise ValueError(
        ErrorMessages.MISSING_DATA(["POSTGRESQL_CONNECTION_STRING"],))

# Initiate a Flask application.
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": [
    "http://localhost:3000",
    "https://www.shahtech.info"
    ]}})

app.config["SQLALCHEMY_DATABASE_URI"] = EnvVars.POSTGRESQL_CONNECTION_STRING

db.init_app(app)

with app.app_context():
    db.create_all()

# Register the blueprint of all the routes.
# API calls for the assigned url prefix will be redirected to the routes.
app.register_blueprint(routes, url_prefix="/")

if __name__ == "__main__":

    if EnvVars.PORT:
        # Run the application.
        app.run(host="0.0.0.0", debug=True, port=EnvVars.PORT)