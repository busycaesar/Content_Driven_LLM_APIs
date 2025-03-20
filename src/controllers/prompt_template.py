from utils import ErrorMessages

class PromptTemplateController:
    def __init__(self, user_id, collection_id):
        self.user_id = user_id
        self.collection_id = collection_id

    async def update(self, prompt_template):
        if not self.user_id or not self.collection_id or not prompt_template:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["user_id", "collection_id", "prompt_template"],
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