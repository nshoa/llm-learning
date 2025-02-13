from fastapi import APIRouter

from api.chatbot.controllers.chatbot import chatbot_router
from api.root import root_router

routers = APIRouter(redirect_slashes=False)

routers.include_router(root_router)
routers.include_router(chatbot_router, prefix="/chatbot")
