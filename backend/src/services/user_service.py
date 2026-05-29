import jwt as pyjwt
from werkzeug.security import generate_password_hash, check_password_hash
from utils import ErrorMessages, EnvVars
from models import User, UserAPIKey, UserContent, ContentLLM, ContentPromptTemplate, VectorStoreModel

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

        user = User.get_by_id(self.user_id)

        if not user:
            raise ValueError("User not found.")

        if not check_password_hash(user.hashed_password, old_password):
            raise ValueError("Current password is incorrect.")

        user.update_password(generate_password_hash(new_password))

    async def get_user(self):
        user = User.get_by_id(self.user_id)

        if not user:
            raise ValueError("User not found.")

        return {
            "name": user.name,
            "email": user.email,
            "created_on": user.created_on.isoformat(),
        }

    async def delete_user(self):
        collection_ids = UserContent.get_all_collection_id(self.user_id)

        for collection_id in collection_ids:
            VectorStoreModel(collection_id).delete()
            ContentLLM(collection_id).delete()
            ContentPromptTemplate(collection_id).delete()
            UserContent(self.user_id, collection_id).delete()

        UserAPIKey.delete_by_user_id(self.user_id)

        user = User.get_by_id(self.user_id)
        
        if not user:
            raise ValueError("User not found.")
        
        user.delete()