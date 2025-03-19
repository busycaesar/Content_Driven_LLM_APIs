from service.content import add_content

async def store_new_content(user_id, content):
    # Make sure that the user id and content is present.
    if not user_id or not content:
        raise ValueError("Both user id and content must be provided. Please check the requirements of this API.")
    
    collection_id = await add_content(user_id, content)

    return collection_id

async def get_all_content(user_id):
    return True

async def get_stored_content(user_id, content_id):
    return True

async def update_stored_content(user_id, content_id, content):
    return True

async def delete_stored_content(user_id, content_id):
    return True