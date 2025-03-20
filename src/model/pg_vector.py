from model.vector_db import get_vector_store, split_content

class PGVector:
    @staticmethod
    def store_new_content(collection_name, content):
        # Split the content.
        splitted_content = split_content(content, 1000, 250)

        # Get the vector store instance by passing the name collection name.
        vector_store = get_vector_store(collection_name)

        # Figure out how to get the collection id of the stored document.
        vector_store.add_documents(splitted_content)

        # Get collection id using the collection name.
        collection_id = 1

        return collection_id