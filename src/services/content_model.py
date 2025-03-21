from utils import ErrorMessages
from .content import ContentService

class ContentModelService:
    def __init__(self, user_id, collection_id):
        if not user_id or not collection_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["user_id", "collection_id"],
                    "Service layer error."
                )
            )

        self.user_id = user_id
        self.collection_id = collection_id

    async def update(self, model_id):
        if not model_id:
            raise ValueError(ErrorMessages.MISSING_DATA(
                    ["model_id"],
                    "Service layer error."
            ))
        
        # Make sure that the content is owned by the same user.
        await ContentService.validate_content_ownership(
            self.user_id, 
            self.collection_id
        )
        
        # Update the model for the content using the collection id.

    async def get(self):
        # Get the model set for the content using the collection id.
        content_model = ""

        return content_model