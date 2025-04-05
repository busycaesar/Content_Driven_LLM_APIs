from utils import ErrorMessages
from .content_service import ContentService

class PromptTemplateService:
    def __init__(self, user_id, collection_id):
        if not user_id or not collection_id:
            raise ValueError(ErrorMessages.MISSING_DATA(
                    ["user_id", "collection_id"],
                    "Controller layer error."
            ))

        self.user_id = user_id
        self.collection_id = collection_id

    async def update(self, prompt_template):
        await ContentService.validate_content_ownership(self.user_id, self.collection_id)

        if not prompt_template:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["prompt_template"],
                    "Controller layer error."
                )
            )
        
        # Update the prompt template using the collection id.

    async def get(self):
        # Get the prompt template using the collection id.
        prompt_template = ""

        return prompt_template