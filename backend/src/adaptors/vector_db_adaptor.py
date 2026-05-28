from langchain_postgres import PGVector
from utils import EnvVars

class VectorDBAdaptor:
    def __init__(self, collection_name, embedding_model):
        if not EnvVars.POSTGRESQL_CONNECTION_STRING or not EnvVars.GEMINI_API_KEYS:
            raise ValueError("Postgres connection string or gemini api keys are nt provided.")

        self.vector_db = PGVector(
            embeddings=embedding_model,
            connection=EnvVars.POSTGRESQL_CONNECTION_STRING,
            collection_name=collection_name,
            use_jsonb=True
        )

    def store_document(self, content):
        self.vector_db.add_documents(content)

    def get_relevant_chunks(self, string, number_of_chunks_required):
        chunks = self.vector_db.similarity_search(string, number_of_chunks_required)

        relevant_chunks = " ".join([chunk.page_content for chunk in chunks])

        return relevant_chunks or ""

    def delete_collection(self):
        self.vector_db.delete_collection()