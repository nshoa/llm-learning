import os

from langchain_community.document_loaders import PDFMinerLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import RAW_DOCS_DIR
from core.common.vector_database import vector_store


class PDFEmbeddingService:
    def __init__(self):
        self.raw_docs_dir = RAW_DOCS_DIR
        self.vector_store = vector_store

    def get_embedding(self, file_name: str):
        absolute_file_path = os.path.join(self.raw_docs_dir, file_name)
        loader = PDFMinerLoader(absolute_file_path)
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
