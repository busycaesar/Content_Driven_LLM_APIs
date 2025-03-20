from utils import ErrorMessages

class UserController:
    def __init__(self, user_id=None):
        self.user_id = user_id

    @staticmethod
    async def register_user(name, email, password):
        if not name or not email or not password:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["name", "email", "password"],
                    "Controller layer error."
                )
            )
        
        return True
        
    @staticmethod
    async def validate_user(email, password):
        if not email or not password:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["email", "password"],
                    "Controller layer error."
                )
            )
        
        return True

    async def update_password(self, old_password, new_password):
        if not self.user_id or not old_password or not new_password:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["user_id", "old_password", "new_password"],
                    "Controller layer error."
                )
            )
        
        return True

    async def get_user(self):
        if not self.user_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["user_id"],
                    "Controller layer error."
                )
            )
                
        return True

    async def delete_user(self):
        if not self.user_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["user_id"],
                    "Controller layer error."
                )
            )
                
        return True