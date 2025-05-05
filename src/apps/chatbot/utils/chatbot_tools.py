from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode

from src.core.common.vector_database import vector_store

pg_vector_retriever = vector_store.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"score_threshold": 0.3, "k": 10},
)


@tool(response_format="content_and_artifact")
def retrieve_from_database(query: str):
    """Use this tool to retrieve information related to the query"""
    retrieved_docs = pg_vector_retriever.invoke(query)
    serialized = "\n\n".join(
        f"Source: {doc.metadata}\n" f"Content: {doc.page_content}" for doc in retrieved_docs
    )

    return serialized, retrieved_docs


tools = ToolNode([retrieve_from_database])
