from fastapi import APIRouter

root_router = APIRouter(
    prefix="",  # Điều này đảm bảo prefix luôn bắt đầu bằng "/"
    tags=["root"],
)


@root_router.get("/")
async def root():
    return {"message": "Welcome to the FastAPI LLM Chatbot!"}
