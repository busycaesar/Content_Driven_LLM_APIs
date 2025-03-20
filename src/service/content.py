from model.user_content import UserContent
from model.pg_vector import PGVector
import uuid

def get_new_collection_name(user_id):
    return f"{user_id}/{uuid.uuid4().hex}"

async def add_content(user_id, content):
    # Get a new collection name.
    collection_name = get_new_collection_name(user_id)

    # Store the content and get the collection id.
    collection_id = PGVector.store_new_content(collection_name,content)

    # Store the collection id and user id in the userc content table.
    
    # Return the collection id.
    return collection_id