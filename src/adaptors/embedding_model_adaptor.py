from langchain_google_genai import GoogleGenerativeAIEmbeddings
from utils import EnvVars

class EmbeddingModelAdaptor:
    def __init__(self):
        self.embedding_model = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=EnvVars.GEMINI_API_KEYS
        )

    def __getattr__(self, name):
        return getattr(self.embedding_model, name)