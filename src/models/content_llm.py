from .db import db
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from utils import ErrorMessages

class ContentLLM(db.Model):
    __tablename__ = "content_llm"

    collection_id = Column(String(32), primary_key=True, nullable=False,unique=True)
    llm_id = Column(Integer, nullable=False)
    created_on = Column(DateTime, nullable=False, default=func.now())
    modified_on = Column(DateTime, onupdate=func.now())

    def __init__(self, collection_id, llm_id):
        if not collection_id or not llm_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["collection_id", "llm_id"],
                    "Model layer error."
                )
            )
        
        self.collection_id = collection_id
        self.llm_id = llm_id

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise ValueError(ErrorMessages.EXCEPTION(
                f"saving the content llm. {str(e)}."
            ))
        
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise ValueError(ErrorMessages.EXCEPTION(
                f"deleting the content llm. {str(e)}."
            ))