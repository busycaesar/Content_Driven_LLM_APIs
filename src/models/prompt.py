from models.db import db
from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func
from utils import ErrorMessages

class Prompt(db.Model):
    __tablename__ = "prompt"

    id = Column(Integer, primary_key=True, autoincrement=True)
    conversation_id = Column(Integer, nullable=False)
    user_prompt = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    created_on = Column(DateTime, nullable=False, default=func.now())
    modified_on = Column(DateTime, onupdate=func.now())

    def __init__(self):
        pass