class ContentModelController:
    def __init__(self, user_id=None, collection_id=None):
        self.user_id = user_id
        self.collection_id = collection_id

    async def update(self, model_id):
        if not self.user_id or not self.collection_id or not model_id:
            raise ValueError("User id, collection id and model_id must be provided. Please check the requirements of this API.")

        return True

    async def get(self):
        if not self.user_id or not self.collection_id:
            raise ValueError("User id and collection id must be provided. Please check the requirements of this API.")

        return True