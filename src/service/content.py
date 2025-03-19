from model.user_content import UserContent

async def add_content(user_id, content):
    user_content = UserContent(user_id)
    
    collection_id = user_content.store_new_content(content)

    return collection_id