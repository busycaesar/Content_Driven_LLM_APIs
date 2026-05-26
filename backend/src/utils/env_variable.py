import os
from dotenv import load_dotenv

load_dotenv()

class EnvVars:
    PORT = os.getenv("PORT")

    # POSTGRESQL
    POSTGRESQL_USER = os.getenv("POSTGRES_USER")
    POSTGRESQL_PASSWD = os.getenv("POSTGRES_PASSWORD")
    POSTGRESQL_DB = os.getenv("POSTGRES_DB")
    POSTGRESQL_URL = os.getenv("POSTGRES_URL")
    POSTGRESQL_CONNECTION_STRING = f"postgresql+psycopg://{POSTGRESQL_USER}:{POSTGRESQL_PASSWD}@{POSTGRESQL_URL}/{POSTGRESQL_DB}"
    
    # GEMINI
    GEMINI_API_KEYS = os.getenv("GEMINI_API_KEY")

    # JWT
    JWT_SECRET = os.getenv("JWT_SECRET")