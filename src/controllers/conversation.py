from utils import ErrorMessages

class ConversationController:
    def __init__(self, user_id, collection_id, conversation_id=None):
        if not user_id or not collection_id:
            raise ValueError(ErrorMessages.MISSING_DATA(
                    ["user_id", "collection_id"],
                    "Controller layer error."
            ))

        self.user_id = user_id
        self.collection_id = collection_id
        self.conversation_id = conversation_id
        
    def _validate_conversation_id(self):
        if not self.conversation_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["conversation_id"],
                    "Controller layer error."
                )
            )        

    async def add(self, prompt):
        if not prompt:
            raise ValueError(ErrorMessages.MISSING_DATA(
                    ["user_id", "collection_id"],
                    "Controller layer error."
            ))

        if not self.conversation_id:
            self.conversation_id = await self._start()

        prompt_response = await self._add_prompt(prompt)

        return prompt_response

    async def _start(self):
        return True

    async def _add_prompt(self, prompt):
        self._validate_conversation_id()

        if not prompt:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["prompt"],
                    "Controller layer error."
                )
            )

        return True

    async def get(self):
        self._validate_conversation_id()

        return True