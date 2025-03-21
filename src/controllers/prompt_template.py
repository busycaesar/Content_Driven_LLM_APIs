from utils import ErrorMessages
from services import PromptTemplateService, ContentService

class PromptTemplateController:
    def __init__(self, user_id, collection_id):
        if not user_id or not collection_id:
            raise ValueError(ErrorMessages.MISSING_DATA(
                    ["user_id", "collection_id"],
                    "Controller layer error."
            ))

        self.user_id = user_id
        self.collection_id = collection_id

        self.prompt_template_service = PromptTemplateService(
            self.user_id,
            self.collection_id
        )

    async def update(self, prompt_template):
        if not prompt_template:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["prompt_template"],
                    "Controller layer error."
                )
            )
        
        await ContentService.validate_content_ownership(
            self.user_id,self.collection_id
        )
        
        await self.prompt_template_service.update(prompt_template)

    async def get(self):
        return await self.prompt_template_service.get()