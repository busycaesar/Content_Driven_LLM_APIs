from langchain_postgres import PGVector
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from utils.env_variable import postgres_connection_string, gemini_api_keys
from langchain.schema import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter

def get_vector_store(collection_name):
    if not postgres_connection_string or not gemini_api_keys:
        raise ValueError("Postgres connection string or gemini api keys are nt provided.")
    
    embedding_model = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=gemini_api_keys
    )

    return PGVector(
        embeddings=embedding_model,
        connection=postgres_connection_string,
        collection_name=collection_name,
        use_jsonb=True
    )

def split_content(content, chunk_size=None, chunk_overlap=None, separator=None):
    if not separator and (not chunk_size or not chunk_overlap):
        raise ValueError("Either separator or chunk size and chunk overlap should be provided.")

    # Convert the text into Document type.
    content = Document(page_content=content)

    if separator:
        text_splitter = CharacterTextSplitter(
            separator=separator,
            is_separator_regex=False
        )
    else:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    # Use the text splitter to split the content into chunks.
    return text_splitter.split_documents([content])