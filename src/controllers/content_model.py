from utils import ErrorMessages 

class ContentModelController:
    def __init__(self, user_id, collection_id):
        if not user_id or not collection_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["user_id", "collection_id"],
                    "Controller layer error."
                )
            )

        self.user_id = user_id
        self.collection_id = collection_id

    async def update(self, model_id):
        if not model_id:
            raise ValueError(ErrorMessages.MISSING_DATA(
                    ["model_id"],
                    "Controller layer error."
            ))

        return True

    async def get(self):
        return True