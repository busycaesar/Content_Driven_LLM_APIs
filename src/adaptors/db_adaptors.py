from utils import ErrorMessages
from flask_sqlalchemy import SQLAlchemy

class DBAdaptor:
    def __init__(self, connection_string):
        if not connection_string:
            raise ValueError(ErrorMessages.MISSING_DATA(
                ["connection_string"],
                "Adaptor level error."
            ))
        
        self.connection_string = connection_string
        self.db = SQLAlchemy()

    def config_app(self, app):
        app.config["SQLALCHEMY_DATABASE_URI"] = self.connection_string

        self.db.init_app(app)

        with app.app_context():
            self.db.create_all()

    def add_sample_data(self, app, seed_function):
        with app.app_context():
            seed_function()

    def __getattr__(self, name):
        return getattr(self.db, name)
