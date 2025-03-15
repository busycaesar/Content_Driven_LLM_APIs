from flask import Flask
from env_variable import port
from flask_cors import CORS

# Import all the routes.
from view import routes

# Initiate a Flask application.
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": [\
    "http://localhost:3000",
    "https://www.shahtech.info"
    ]}})

# Register the blueprint of all the routes.
# API calls for the assigned url prefix will be redirected to the routes.
app.register_blueprint(routes, url_prefix="/")

if __name__ == "__main__":

    if port:
        # Run the application.
        app.run(host="0.0.0.0",debug=True, port=port)