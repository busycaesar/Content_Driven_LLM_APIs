from utils import EnvVars
from app import app

if __name__ == "__main__":

    if EnvVars.PORT:
        # Run the application.
        app.run(host="0.0.0.0", debug=True, port=EnvVars.PORT)