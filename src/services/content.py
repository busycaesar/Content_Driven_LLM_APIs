from models import VectorStoreModel
from utils import ConfigVars
import uuid

def get_new_collection_name(user_id):
    return f"{user_id}/{uuid.uuid4().hex}"

async def add_content(user_id, content):
    # Get a new collection name.
    collection_name = get_new_collection_name(user_id)

    vector_store = VectorStoreModel()

    # Store the content and get the collection id.
    collection_id = vector_store.store_new_content(
        collection_name,
        content,
        ConfigVars.CHUNK_SIZE,
        ConfigVars.CHUNK_OVERLAP
    )

    # Store the collection id and user id in the user content table.
    
    # Return the collection id.
    return collection_id