from .db import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import func
from utils import ErrorMessages

class LLM(db.Model):
    __tablename__ = "llm"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False, unique=True)

    def __init__(self):
        pass