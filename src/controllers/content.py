from services import ContentService
from utils import ErrorMessages

class ContentController:
    def __init__(self, user_id=None, collection_id=None):
        self.user_id = user_id
        self.collection_id = collection_id

    async def add(self, content):
        if not self.user_id or not content:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["user_id", "content"],
                    "Controller layer error."
                )
            )
        
        content_service = ContentService(self.user_id)
    
        self.collection_id = await content_service.add(content)

        return self.collection_id

    async def get_all(self):
        if not self.user_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["user_id"],
                    "Controller layer error."
                )
            )

        return True

    async def get(self):
        if not self.user_id or not self.collection_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["user_id", "collection_id"],
                    "Controller layer error."
                )
            )
        
        return True

    async def update(self, content):
        if not self.user_id or not self.collection_id or not content:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["user_id", "collection_id", "content"],
                    "Controller layer error."
                )
            )
        
        return True

    async def delete(self):
        if not self.user_id or not self.collection_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["user_id", "collection_id"],
                    "Controller layer error."
                )
            )

        return True