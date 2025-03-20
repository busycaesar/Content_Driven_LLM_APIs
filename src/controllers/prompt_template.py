from utils import ErrorMessages

class PromptTemplateController:
    def __init__(self, user_id, collection_id):
        if not user_id or not collection_id:
            raise ValueError(ErrorMessages.MISSING_DATA(
                    ["user_id", "collection_id"],
                    "Controller layer error."
            ))

        self.user_id = user_id
        self.collection_id = collection_id

    async def update(self, prompt_template):
        if not prompt_template:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["prompt_template"],
                    "Controller layer error."
                )
            )

        return True

    async def get(self):
        return True