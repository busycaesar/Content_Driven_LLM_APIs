from .db import db
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from utils import ErrorMessages

class User(db.Model):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(20), nullable=False)
    email = Column(String(20), nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    created_on = Column(DateTime, nullable=False, default=datetime.utcnow)
    modified_on = Column(DateTime, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    is_delete = Column(Boolean, default=False)

    def __init__(self, name, email, hashed_password):
        if not name or not email or not hashed_password:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["name", "email", "hashed_password"],
                    "Model layer error."
                )
            )

        self.name = name
        self.email = email
        self.hashed_password = hashed_password

    @staticmethod
    def get_by_id(user_id):
        return db.session.query(User).filter_by(id=user_id).first()

    @staticmethod
    def get_by_email(email):
        return db.session.query(User).filter_by(email=email).first()

    def update_password(self, hashed_password):
        try:
            self.hashed_password = hashed_password
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise ValueError(ErrorMessages.EXCEPTION(
                f"updating the user password. {str(e)}."
            )) from e

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise ValueError(ErrorMessages.EXCEPTION(
                f"saving the user. {str(e)}."
            )) from e

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise ValueError(ErrorMessages.EXCEPTION(
                f"deleting the user. {str(e)}."
            )) from e