from utils import ErrorMessages, ConfigVars
from adaptors import LLMAdaptor
from services import ContentService
from models import Conversation, VectorStoreModel, ContentPromptTemplate, ContentLLM, LLM, Prompt, UserAPIKey

class ConversationService:
    def __init__(self, api_key, collection_id, conversation_id=None):
        if not api_key or not collection_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["api_key", "collection_id"],
                    "Service layer error."
                )
            )
        
        self.api_key = api_key
        self.user_id = None
        self.collection_id = collection_id
        self.conversation_id = conversation_id

    async def _get_user_id(self):
        user_api_key = UserAPIKey(self.api_key)

        self.user_id = user_api_key.get_user_id()

        if not self.user_id:
            raise ValueError(ErrorMessages.NOT_FOUND("Invalid API Key."))
        
    def _validate_conversation_id(self):
        if not self.conversation_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["conversation_id"],
                    "Service layer error."
                )
            )

    async def start(self):
        await self._get_user_id()

        await ContentService.validate_content_ownership(
            self.user_id,
            self.collection_id
        )
        
        # Initiate a new conversation, store the conversation id and return it.
        conversation = Conversation(self.collection_id)
        
        self.conversation_id = conversation.save()

        return self.conversation_id

    async def add_prompt(self, prompt):
        await self._get_user_id()

        await ContentService.validate_content_ownership(
            self.user_id,
            self.collection_id
        )

        self._validate_conversation_id()

        if not prompt:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["prompt"],
                    "Service layer error."
                )
            )
        
        # In case of adding a prompt in existing conversation, the collection id would not be stored in the class.
        if not self.collection_id:
            self.collection_id = Conversation.get_collection_id(self.conversation_id)

        # Get the relevant content using the collection id.
        vector_store_model = VectorStoreModel(self.collection_id)

        relevant_content = vector_store_model.get_relevant_content(
            prompt,
            ConfigVars.DEFAULT.RELEVANT_CHUNKS_REQUIRED
        )

        # Get the prompt template for the content.
        content_prompt_template = ContentPromptTemplate(self.collection_id)

        prompt_template = content_prompt_template.get()

        # Get the model to be used for the content.
        content_llm = ContentLLM(self.collection_id)
        
        llm_id = content_llm.get()

        model_name = LLM.get(llm_id)

        # Get the response using the prompt, relevant chunk of data, prompt template and model.
        llm_adaptor = LLMAdaptor(model_name)

        response = llm_adaptor.generate_response(
            prompt,
            relevant_content,
            prompt_template
        )

        print("response",response)

        # Store the response into the database and return the response.
        prompt = Prompt(self.conversation_id, prompt, response)

        prompt.save()

        return response

    async def get(self):
        self._validate_conversation_id()

        prompt = Prompt(self.conversation_id)

        # Get the prompt-response using the collection id and return it.
        conversation = prompt.get_conversation()

        return conversation