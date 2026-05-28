from .db import db
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from utils import ErrorMessages

class UserAPIKey(db.Model):
    __tablename__ = "user_api_key"

    user_id = Column(String(32), primary_key=True, nullable=False, unique=True)
    api_key = Column(String(32), nullable=False, unique=True)
    created_on = Column(DateTime, nullable=False, default=datetime.utcnow)

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

    def _get_record(self):
        return db.session.query(UserAPIKey).filter_by(api_key=self.api_key).first()

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
        record = self._get_record()

        return record.user_id or None

    def revoke(self):
        try:
            record = self._get_record()
            
            if not record: return
            
            db.session.delete(record)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise ValueError(ErrorMessages.EXCEPTION(
                f"deleting the user api key. {str(e)}."
            )) from e

    @staticmethod
    def delete_for_user(user_id):
        try:
            record = db.session.query(UserAPIKey).filter_by(user_id=user_id).first()
            
            if not record: return

            db.session.delete(record)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise ValueError(ErrorMessages.EXCEPTION(
                f"deleting the user api key. {str(e)}."
            )) from e