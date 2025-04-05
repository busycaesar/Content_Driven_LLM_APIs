from .db import db
from sqlalchemy import Column, Integer, String
from utils import ErrorMessages

class LLM(db.Model):
    __tablename__ = "llm"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False, unique=True)

    @staticmethod
    def get_all():
        pass

    @staticmethod
    def get(llm_id):
        llm = db.session.query(LLM).filter_by(
            id=llm_id
        ).first()

        return llm.name if llm.name else None