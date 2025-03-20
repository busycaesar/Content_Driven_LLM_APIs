class ConversationController:
    def __init__(self, user_id=None, collection_id=None, conversation_id=None):
        self.user_id = user_id
        self.collection_id = collection_id
        self.conversation_id = conversation_id

    async def add(self, prompt):
        if not prompt:
            raise ValueError("Prompt must be provided. Please check the requirements of this API.")

        if not self.conversation_id:
            self.conversation_id = await self._start()

        await self._add_prompt(prompt)

    async def _start(self):
        if not self.user_id or not self.collection_id:
            raise ValueError("Both user id and collection id must be provided. Please check the requirements of this API.")

        return True

    async def _add_prompt(self, prompt):
        if not self.conversation_id or not prompt:
            raise ValueError("Both conversation id and prompt must be provided. Please check the requirements of this API.")

        return True

    async def get(self):
        if not self.conversation_id:
            raise ValueError("Conversation id must be provided. Please check the requirements of this API.")

        return True