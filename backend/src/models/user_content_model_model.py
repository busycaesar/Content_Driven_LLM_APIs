from .db import db
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from utils import ErrorMessages

class UserContent(db.Model):
    __tablename__ = "user_content"

    user_id = Column(String(32), nullable=False)
    collection_id = Column(String(32), primary_key=True, nullable=False, unique=True)
    created_on = Column(DateTime, nullable=False, default=datetime.utcnow)
    modified_on = Column(DateTime, onupdate=datetime.utcnow)

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

    def _get_record(self):
        return db.session.query(UserContent).filter_by(collection_id=self.collection_id).first()

    @staticmethod
    def get_all_collection_id(user_id):
        # Get all the collection ids of the user using the user id.
        collection_ids = []

        # Return all the collection ids of the user.
        return collection_ids
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise ValueError(ErrorMessages.EXCEPTION(
                f"saving the user content's collection id. {str(e)}."
            )) from e

    def delete(self):
        try:
            record = self._get_record()
            
            if not record: return

            db.session.delete(record)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise ValueError(ErrorMessages.EXCEPTION(
                f"deleting the user content's collection id. {str(e)}."
            )) from e