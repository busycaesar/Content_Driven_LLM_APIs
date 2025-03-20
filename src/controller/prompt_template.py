class PromptTemplateController:
    def __init__(self, user_id, collection_id):
        self.user_id = user_id
        self.collection_id = collection_id

    async def update(self, prompt_template):
        if not self.user_id or not self.collection_id or not prompt_template:
            raise ValueError("User id, collection id and prompt template must be provided. Please check the requirements of this API.")

        return True

    async def get(self):
        if not self.user_id or not self.collection_id:
            raise ValueError("Both user id and collection must be provided. Please check the requirements of this API.")

        return True