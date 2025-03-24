from .db import db
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func
from utils import ErrorMessages

class Conversation(db.Model):
    __tablename__ = "conversation"

    id = Column(Integer, primary_key=True, autoincrement=True)
    collection_id = Column(Integer, nullable=False)
    created_on = Column(DateTime, nullable=False, default=func.now())
    modified_on = Column(DateTime, onupdate=func.now())

    def __init__(self):
        pass