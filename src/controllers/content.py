from services import ContentService
from utils import ErrorMessages

class ContentController:
    def __init__(self, user_id, collection_id=None):
        if not user_id:
            raise ValueError(ErrorMessages.MISSING_DATA(
                    ["user_id"],
                    "Controller layer error."
            ))
        
        self.user_id = user_id
        self.collection_id = collection_id

    async def add(self, content):
        if not content:
            raise ValueError(ErrorMessages.MISSING_DATA(
                    ["content"],
                    "Controller layer error."
            ))
        
        content_service = ContentService(self.user_id)
    
        self.collection_id = await content_service.add(content)

        return self.collection_id

    async def get_all(self):
        return True

    async def get(self):
        if not self.collection_id:
            raise ValueError(ErrorMessages.MISSING_DATA(
                    ["collection_id"],
                    "Controller layer error."
            ))
        
        return True

    async def update(self, content):
        if not self.collection_id or not content:
            raise ValueError(ErrorMessages.MISSING_DATA(
                    ["collection_id", "content"],
                    "Controller layer error."
            ))
        
        return True

    async def delete(self):
        if not self.collection_id:
            raise ValueError(ErrorMessages.MISSING_DATA(
                    ["collection_id"],
                    "Controller layer error."
            ))

        return True