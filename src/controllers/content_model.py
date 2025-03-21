from utils import ErrorMessages
from services import ContentModelService, ContentService

class ContentModelController:
    def __init__(self, user_id, collection_id):
        if not user_id or not collection_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["user_id", "collection_id"],
                    "Controller layer error."
                )
            )

        self.user_id = user_id
        self.collection_id = collection_id

        self.content_model_service = ContentModelService(
            self.user_id,
            self.collection_id
        )

    async def update(self, model_id):
        if not model_id:
            raise ValueError(ErrorMessages.MISSING_DATA(
                    ["model_id"],
                    "Controller layer error."
            ))
        
        await ContentService.validate_content_ownership(self.user_id, self.collection_id)
        
        await self.content_model_service.update(model_id)

    async def get(self):
        await self.content_model_service.get()