from db.vector_db import get_vector_store, split_content

class UserContent:
    def __init__(self, user_id):
        self.user_id = user_id

    def store_new_content(self, content):
        # Split the content.
        splitted_content = split_content(content, 1000, 250)

        # Generate collection name
        collection_name = 'collection_name2'

        # Get the vector store instance.
        vector_store = get_vector_store(collection_name)

        # Figure out how to get the collection id of the stored document.
        vector_store.add_documents(splitted_content)

        # Get collection id using the collection name.
        collection_id = 1

        return collection_id

    def get_all_content(self):
        # Get all the collection id of the user.
        # Get the content using the collection ids of the user.
        # Return all the content.
        return ["All Content", "Of the user"]

    def update_content(self, collection_id, content):
        # Get the vector store instance.

        # Update the content.
        return
    
    def delete_content(self, collection_id):
        # Get the vector store instance.

        # Delete the content.
        return
