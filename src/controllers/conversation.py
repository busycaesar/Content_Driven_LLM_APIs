from utils import ErrorMessages
from services import ConversationService

class ConversationController:
    def __init__(self, user_id=None, collection_id=None, conversation_id=None):
        self.user_id = user_id
        self.collection_id = collection_id
        self.conversation_id = conversation_id

        self.conversation_service = ConversationService(
            self.user_id,
            self.collection_id,
            self.conversation_id
        )
        
    def _validate_user_data(self):
        if not self.user_id or not self.collection_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["user_id", "collection_id"],
                    "Controller layer error."
                )
            )

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
                    ["prompt"],
                    "Controller layer error."
            ))
        
        self._validate_user_data()

        if not self.conversation_id:
            await self._start()

        self._validate_conversation_id()

        prompt_response = await self._add_prompt(prompt)

        return prompt_response

    async def _start(self):
        self.conversation_id = await self.conversation_service.start()

    async def _add_prompt(self, prompt):
        response = await self.conversation_service.add_prompt(prompt)

        return response

    async def get(self):
        self._validate_conversation_id()

        conversation = await self.conversation_service.get()

        return conversation