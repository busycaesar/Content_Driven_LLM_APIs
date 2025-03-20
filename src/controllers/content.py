from service.content import add_content

class ContentController:
    def __init__(self, user_id=None, collection_id=None):
        self.user_id = user_id
        self.collection_id = collection_id

    async def add(self, content):
        if not self.user_id or not content:
            raise ValueError("Both user id and content must be provided. Please check the requirements of this API.")
    
        self.collection_id = await add_content(self.user_id, content)

        return self.collection_id

    async def get_all(self):
        if not self.user_id:
            raise ValueError("collection id must be provided. Please check the requirements of this API.")

        return True

    async def get(self):
        if not self.user_id or not self.collection_id:
            raise ValueError("Both user id and collection id must be provided. Please check the requirements of this API.")
        
        return True

    async def update(self, content):
        if not self.user_id or not self.collection_id or not content:
            raise ValueError("User id, collection id and content must be provided. Please check the requirements of this API.")
        
        return True

    async def delete(self):
        if not self.user_id or not self.collection_id:
            raise ValueError("Both user id and collection id must be provided. Please check the requirements of this API.")

        return True