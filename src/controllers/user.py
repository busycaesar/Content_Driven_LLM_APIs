from utils import ErrorMessages
from services import UserService

class UserController:
    def __init__(self, user_id):
        if not user_id:
            raise ValueError(ErrorMessages.MISSING_DATA(
                    ["user_id"],
                    "Controller layer error."
            ))

        self.user_id = user_id

        self.user_service = UserService(self.user_id)

    @staticmethod
    async def register_user(name, email, password):
        if not name or not email or not password:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["name", "email", "password"],
                    "Controller layer error."
                )
            )
        
        jwt = await UserService.register_user(name, email, password)
        
        return jwt
        
    @staticmethod
    async def validate_user(email, password):
        if not email or not password:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["email", "password"],
                    "Controller layer error."
                )
            )
        
        jwt = await UserService.validate_user(email, password)
        
        return jwt

    async def update_password(self, old_password, new_password):
        if not old_password or not new_password:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["old_password", "new_password"],
                    "Controller layer error."
                )
            )
        
        await self.user_service.update_password(old_password, new_password)
        
    async def get_user(self):
        return await self.user_service.get_user()

    async def delete_user(self):
        self.user_service.delete_user()