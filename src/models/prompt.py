from .db import db
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from utils import ErrorMessages

class Prompt(db.Model):
    __tablename__ = "prompt"

    id = Column(Integer, primary_key=True, autoincrement=True)
    conversation_id = Column(Integer, nullable=False)
    user_prompt = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    created_on = Column(DateTime, nullable=False, default=func.now())
 
    def __init__(self, conversation_id, user_prompt=None, response=None):
        if not conversation_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["conversation_id"],
                    "Model layer error."
                )
            )
        
        self.conversation_id = conversation_id
        self.user_prompt = user_prompt
        self.response = response

    def _validate_prompt_data(self):
        if not self.user_prompt or not self.response:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["user_prompt", "response"],
                    "Model layer error."
                )
            )
        
    def save(self):
        try:
            self._validate_prompt_data()

            db.session.add(self)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise ValueError(ErrorMessages.EXCEPTION(
                f"saving the prompt. {str(e)}."
            )) from e