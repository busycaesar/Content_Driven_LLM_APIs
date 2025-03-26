from .db import db
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from utils import ErrorMessages

class User(db.Model):
    __tablename__ = "user"

    id = Column(String(32), primary_key=True, nullable=False)
    name = Column(String(20), nullable=False)
    email = Column(String(20), nullable=False, unique=True)
    created_on = Column(DateTime, nullable=False, default=func.now())
    modified_on = Column(DateTime, onupdate=func.now())
    is_active = Column(Boolean, default=True)
    is_delete = Column(Boolean, default=False)

    def __init__(self):
        pass