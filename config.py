import os

from dotenv import load_dotenv

load_dotenv()

# APP
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
API_PORT = int(os.getenv("API_PORT"))
CORS_ALLOWED_ORIGINS: list = [
    *(filter(lambda x: len(x) > 0, os.getenv("CORS_ALLOWED_ORIGINS", "").split(",")))
]

# DATABASE
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
VECTOR_DB_COLLECTION_NAME = os.getenv("VECTOR_DB_COLLECTION_NAME")

DATABASE_CONN_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

# LLM
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Embedding
RAW_DOCS_DIR = os.path.join(BASE_DIR, "raw_docs")
