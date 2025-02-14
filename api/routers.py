from fastapi import APIRouter

from api.chatbot.controllers.chatbot import chatbot_router


def create_root_router():
    root_router = APIRouter(
        prefix="",
        tags=["root"],
    )

    @root_router.get("/")
    async def root():
        return {"message": "Welcome to the FastAPI LLM Chatbot!"}

    return root_router


# Main routers setup
routers = APIRouter(redirect_slashes=False)
routers.include_router(chatbot_router, prefix="/chatbot")
routers.include_router(create_root_router())