from models.db import db
from sqlalchemy import func
from datetime import datetime

class UserContent:
    __tablename__ = "user_content"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    collection_id = db.Column(db.Integer, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, default=func.now())
    modified_on = db.Column(db.DateTime, onupdate=func.now())

    def __init__(self, user_id):
        self.user_id = user_id

    def store_new_content(self, content):
        return collection_id

    def get_all_content(self):
        # Get all the collection id of the user.
        # Get the content using the collection ids of the user.
        # Return all the content.
        return ["All Content", "Of the user"]

    def update_content(self, collection_id, content):
        # Get the vector store instance.

        # Update the content.
        return
    
    def delete_content(self, collection_id):
        # Get the vector store instance.

        # Delete the content.
        return
