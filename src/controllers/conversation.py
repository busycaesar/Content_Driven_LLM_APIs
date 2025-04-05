from utils import ErrorMessages
from services import ConversationService

class ConversationController:
    def __init__(self, api_key, collection_id, conversation_id=None):
        if not api_key or not collection_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["api_key", "collection_id"],
                    "Controller layer error."
                )
            )
        
        self.api_key = api_key
        self.collection_id = collection_id
        self.conversation_id = None

        if conversation_id:
            self.conversation_id = int(str(conversation_id))

        self.conversation_service = ConversationService(
            self.api_key,
            self.collection_id,
            self.conversation_id
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

        if not self.conversation_id:
            await self._start()

        self._validate_conversation_id()

        prompt_response = await self._add_prompt(prompt)

        return prompt_response, self.conversation_id

    async def _start(self):
        self.conversation_id = await self.conversation_service.start()

    async def _add_prompt(self, prompt):
        response = await self.conversation_service.add_prompt(prompt)

        return response

    async def get(self):
        self._validate_conversation_id()

        conversation = await self.conversation_service.get()

        return conversation