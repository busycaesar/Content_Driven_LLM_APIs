from models.db import db
from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func
from utils import ErrorMessages

class ContentPromptTemplate(db.Model):
    __tablename__ = "content_prompt_template"

    id = Column(Integer, primary_key=True, autoincrement=True)
    collection_id = Column(Integer, nullable=False)
    prompt_template = Column(Text, nullable=False)
    created_on = Column(DateTime, nullable=False, default=func.now())
    modified_on = Column(DateTime, onupdate=func.now())

    def __init__(self, collection_id):
        if not collection_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["collection_id"],
                    "Model layer error."
                )
            )

        self.collection_id = collection_id