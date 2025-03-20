class UserController:
    def __init__(self, user_id=None):
        self.user_id = user_id

    @staticmethod
    async def register_user(name, email, password):
        if not name or not email or not password:
            raise ValueError("Name, Email and Password must be provided. Please check the requirements of this API.")
        
        return True
        
    @staticmethod
    async def validate_user(email, password):
        if not email or not password:
            raise ValueError("Email and Password must be provided. Please check the requirements of this API.")
        
        return True

    async def update_password(self, old_password, new_password):
        if not self.user_id or not old_password or not new_password:
            raise ValueError("User id, old password and new password must be provided. Please check the requirements of this API.")
        
        return True

    async def get_user(self):
        if not self.user_id:
            raise ValueError("User id must be provided. Please check the requirements of this API.")
                
        return True

    async def delete_user(self):
        if not self.user_id:
            raise ValueError("User id must be provided. Please check the requirements of this API.")
                
        return True