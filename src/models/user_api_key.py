from .db import db
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from utils import ErrorMessages

class UserAPIKey(db.Model):
    __tablename__ = "user_api_key"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(32), nullable=False)
    api_key = Column(String(32), nullable=False)
    created_on = Column(DateTime, nullable=False, default=func.now())
    modified_on = Column(DateTime, onupdate=func.now())

    def __init__(self):
        pass