from .db import db
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from utils import ErrorMessages

class UserAPIKey(db.Model):
    __tablename__ = "user_api_key"

    user_id = Column(String(32), primary_key=True, nullable=False, unique=True)
    api_key = Column(String(32), nullable=False, unique=True)
    created_on = Column(DateTime, nullable=False, default=func.now())

    def __init__(self, api_key, user_id=None):
        if not api_key:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["api_key"],
                    "Model layer error."
                )
            )
        
        self.api_key = api_key
        self.user_id = user_id

    async def _validate_user_id(self):
        if not self.user_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["user_id"],
                    "Model layer error."
                )
            )

    def save(self):
        try:
            self._validate_user_id()

            db.session.add(self)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise ValueError(ErrorMessages.EXCEPTION(
                f"saving the user api keys. {str(e)}."
            )) from e
        
    def get_user_id(self):
        user_api_key = db.session.query(UserAPIKey).filter_by(
            api_key=self.api_key
        ).first()

        return user_api_key.user_id or None