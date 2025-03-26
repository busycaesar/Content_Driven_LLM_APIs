from utils import ErrorMessages

class ConversationService:
    def __init__(self, user_id=None, collection_id=None, conversation_id=None):
        self.user_id = user_id
        self.collection_id = collection_id
        self.conversation_id = conversation_id

    def _validate_user_data(self):
        if not self.user_id or not self.collection_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["user_id", "collection_id"],
                    "Service layer error."
                )
            )
        
    def _validate_conversation_id(self):
        if not self.conversation_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["conversation_id"],
                    "Service layer error."
                )
            )

    async def start(self):
        self._validate_user_data()
        
        # Initiate a new conversation, store the conversation id and return it.
        self.conversation_id = 1

        return self.conversation_id

    async def add_prompt(self, prompt):
        self._validate_conversation_id()

        if not prompt:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["prompt"],
                    "Service layer error."
                )
            )
        
        # Get the relevant content using the collection id.

        # Get the response using the prompt and relevant chunk of data.
        response = ""

        # Store the response into the database and return the response.

        return response

    async def get(self):
        self._validate_conversation_id()

        # Get the prompt-response using the collection id and return it.
        conversation = [{"prompt":"Who is Dev?","response":"Dev is a developer."}]

        return conversation