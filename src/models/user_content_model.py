from .db import db
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from utils import ErrorMessages

class UserContent(db.Model):
    __tablename__ = "user_content"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(32), nullable=False)
    collection_id = Column(String(32), nullable=False)
    created_on = Column(DateTime, nullable=False, default=func.now())
    modified_on = Column(DateTime, onupdate=func.now())

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
    
    def save(self):
        db.session.add(self)
        db.session.commit()