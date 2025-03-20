from utils import ErrorMessages 

class ContentModelController:
    def __init__(self, user_id=None, collection_id=None):
        self.user_id = user_id
        self.collection_id = collection_id

    async def update(self, model_id):
        if not self.user_id or not self.collection_id or not model_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["user_id", "collection_id", "model_id"],
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