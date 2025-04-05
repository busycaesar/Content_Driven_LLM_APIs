from models import VectorStoreModel, UserContent, ContentPromptTemplate, ContentLLM
from utils import ConfigVars, ErrorMessages
import uuid

class ContentService:
    def __init__(self, user_id, collection_id=None):
        if not user_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["user_id"],
                    "Service layer error."
                )
            )

        self.user_id = user_id
        self.collection_id = collection_id

    def _validate_collection_id(self):
        if not self.collection_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["collection_id"],
                    "Service layer error."
                )
            )

    @staticmethod
    async def validate_content_ownership(user_id, collection_id):
        if not user_id or not collection_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["user_id", "collection_id"],
                    "Service layer error."
                )
            )

        # Validate if the content belongs with the user whos id is provided.

        return True

    def _get_new_collection_uuid(self):
        return uuid.uuid4().hex

    async def add(self, content):
        if not content:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["content"],
                    "Service layer error."
                )
            )
        
        # Get a new collection name.
        self.collection_id = self._get_new_collection_uuid()

        # Initiate Vector Store.
        vector_store = VectorStoreModel(self.collection_id)

        # Store the content.
        vector_store.store_new_content(
            content,
            ConfigVars.DEFAULT.CHUNK_SIZE,
            ConfigVars.DEFAULT.CHUNK_OVERLAP
        )

        # Store the collection id and user id in the user content table.
        user_content = UserContent(self.user_id, self.collection_id)

        user_content.save()

        # Store the prompt template with the collection id.
        content_prompt_template = ContentPromptTemplate(
            self.collection_id,
            ConfigVars.DEFAULT.PROMPT_TEMPLATE
        )

        content_prompt_template.save()

        # Store the content llm with the collection id.
        content_llm = ContentLLM(self.collection_id, ConfigVars.DEFAULT.LLM_ID)

        content_llm.save()
    
        # Return the collection id.
        return self.collection_id
    
    async def get_all(self):
        # Get all the collection ids of the user.

        # Get all the content using the collection id.
        content = ["All","The","Content"]

        return content

    async def get(self):
        self._validate_collection_id()

        # Get the content using the collection id.
        content = ""

        return content

    async def update(self, content):
        self._validate_collection_id()

        if not content:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["content"],
                    "Service layer error."
                )
            )
        
        # Update the content using the collection id.

    async def delete(self):
        self._validate_collection_id()

        # Delete the content using the collection id.