from adaptors import EmbeddingModelAdaptor, VectorDBAdaptor, TextSplitterAdaptor
from utils import ErrorMessages

class VectorStoreModel:
    def __init__(self, collection_id):
        if not collection_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["collection_id"],
                    "Model layer error."
                )
            )

        self.collection_id = collection_id
        self.embedding_model = EmbeddingModelAdaptor()
        self.vector_store = VectorDBAdaptor(
            self.collection_id,
            self.embedding_model
        )
    
    def store_new_content(
            self,
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

        # Store the splitter content in the vector store.
        self.vector_store.store_document(splitted_content)