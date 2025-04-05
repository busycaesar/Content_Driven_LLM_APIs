from utils import ErrorMessages

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
        
        # Hash the password of the user.
        
        # Register the new user, generate jwt and return the jwt.
        jwt = ""

        return jwt
        
    @staticmethod
    async def validate_user(email, password):
        if not email or not password:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["email", "password"],
                    "Service layer error."
                )
            )
        
        # Get the stored password of the user using the email.
        stored_password = ""

        # Compare the store password with the received password to make sure that both matches.
        
        # Generate the jwt for the user and return it.
        jwt = ""

        return jwt

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