from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

from config import DATABASE_CONN_URL, OPENAI_API_KEY, VECTOR_DB_COLLECTION_NAME

vector_store = PGVector(
    connection=DATABASE_CONN_URL,
    collection_name=VECTOR_DB_COLLECTION_NAME,
    embeddings=OpenAIEmbeddings(model="text-embedding-3-large", api_key=OPENAI_API_KEY),
    use_jsonb=True,
)
