import jwt as pyjwt
from werkzeug.security import generate_password_hash, check_password_hash
from utils import ErrorMessages, EnvVars
from models import User

class UserService:
    def __init__(self, user_id):
        if not user_id:
            raise ValueError(ErrorMessages.MISSING_DATA(
                    ["user_id"],
                    "Service layer error."
            ))

        self.user_id = user_id

    @staticmethod
    async def register_user(name, email, password):
        if not name or not email or not password:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["name", "email", "password"],
                    "Service layer error."
                )
            )
        
        hashed_password = generate_password_hash(password)

        user = User(name, email, hashed_password)
        user.save()

        token = pyjwt.encode({"user_id": user.id}, EnvVars.JWT_SECRET, algorithm="HS256")

        return token
        
    @staticmethod
    async def validate_user(email, password):
        if not email or not password:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["email", "password"],
                    "Service layer error."
                )
            )
        
        user = User.get_by_email(email)

        if not user or not check_password_hash(user.hashed_password, password):
            raise ValueError("Invalid credentials.")

        token = pyjwt.encode({"user_id": user.id}, EnvVars.JWT_SECRET, algorithm="HS256")

        return token

    async def update_password(self, old_password, new_password):
        if not old_password or not new_password:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["old_password", "new_password"],
                    "Service layer error."
                )
            )
        
        # Hash the new password of the user.

        # Update the password of the user.

    async def get_user(self):
        # Get the information of the user using the user id and return it.
        user_info = {}

        return user_info

    async def delete_user(self):
        # Delete the user account
        return