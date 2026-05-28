from .db import db
from sqlalchemy import Column, Integer, DateTime, String
from datetime import datetime
from utils import ErrorMessages

class Conversation(db.Model):
    __tablename__ = "conversation"

    id = Column(Integer, primary_key=True, autoincrement=True)
    collection_id = Column(String(32), nullable=False)
    created_on = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, collection_id):
        if not collection_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["collection_id"],
                    "Model layer error."
                )
            )
        
        self.collection_id = collection_id

    @staticmethod
    def get_collection_id(conversation_id):
        conversation = db.session.query(Conversation).filter_by(
            id=conversation_id
        ).first()

        return conversation.collection_id if conversation.collection_id else None

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()

            return self.id

        except Exception as e:
            db.session.rollback()
            raise ValueError(ErrorMessages.EXCEPTION(
                f"saving the content llm. {str(e)}."
            )) from e