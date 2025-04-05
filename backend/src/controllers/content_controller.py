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

        self.content_service = ContentService(self.user_id, self.collection_id)

    def _validate_collection_id(self):
        if not self.collection_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["collection_id"],
                    "Controller layer error."
                )
            )

    async def add(self, content):
        if not content:
            raise ValueError(ErrorMessages.MISSING_DATA(
                    ["content"],
                    "Controller layer error."
            ))
        
        self.collection_id = await self.content_service.add(content)

        return self.collection_id

    async def get_all(self):
        content = await self.content_service.get_all()

        return content

    async def get(self):
        self._validate_collection_id()
        
        content = await self.content_service.get()

        return content

    async def update(self, content):
        self._validate_collection_id()

        if not content:
            raise ValueError(ErrorMessages.MISSING_DATA(
                    ["content"],
                    "Controller layer error."
            ))
        
        await self.content_service.update(content)

    async def delete(self):
        self._validate_collection_id()

        await self.content_service.delete()