import os

from langchain_community.document_loaders import PDFMinerLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config import RAW_DOCS_DIR
from src.core.common.vector_database import vector_store


class PDFEmbeddingService:
    def __init__(self, file_name: str):
        self.file_path = os.path.join(RAW_DOCS_DIR, file_name)
        self.vector_store = vector_store

    def get_embedding(self):
        loader = PDFMinerLoader(self.file_path)
        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            add_start_index=True
        )
        all_splits = text_splitter.split_documents(docs)
        print(f"Split blog post into {len(all_splits)} sub-documents.")

        document_ids = vector_store.add_documents(documents=all_splits)
        print(document_ids)
