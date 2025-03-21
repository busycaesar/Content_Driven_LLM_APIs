from adaptors import EmbeddingModelAdaptor, VectorDBAdaptor, TextSplitterAdaptor

class VectorStoreModel:
    def __init__(self, collection_id=None):
        self.collection_id = collection_id

    def __get_vector_store(self, collection_name):
        embedding_model = EmbeddingModelAdaptor()

        return VectorDBAdaptor(collection_name, embedding_model)
    
    def store_new_content(
            self,
            collection_name,
            content,
            chunk_size=None,
            chunk_overlap=None,
            separator=None
        ):
        # Split the content.
        splitted_content = TextSplitterAdaptor.split_content(
            content,
            chunk_size,
            chunk_overlap,
            separator
        )

        # Get the vector store instance by passing the name collection name.
        vector_store = self.__get_vector_store(collection_name)

        # Store the splitter content in the vector store.
        self.collection_id = vector_store.store_document(splitted_content)

        # Return the collection id.
        return self.collection_id