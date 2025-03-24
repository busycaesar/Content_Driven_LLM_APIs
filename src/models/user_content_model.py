from models.db import db
from sqlalchemy import func
from utils import ErrorMessages

class UserContent(db.Model):
    __tablename__ = "user_content"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    collection_id = db.Column(db.Integer, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, default=func.now)
    modified_on = db.Column(db.DateTime, onupdate=func.now)

    def __init__(self, user_id, collection_id):
        if not user_id or not collection_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["user_id", "collection_id"],
                    "Model layer error."
                )
            )

        self.user_id = user_id
        self.collection_id = collection_id

    @staticmethod
    def get_all_collection_id(user_id):
        # Get all the collection ids of the user using the user id.
        collection_ids = []

        # Return all the collection ids of the user.
        return collection_ids
    
    def delete_content(self):
        # Delete the row.
