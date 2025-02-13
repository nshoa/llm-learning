from fastapi import APIRouter, Query

from apps.chatbot.services import ChatbotService

chatbot_router = APIRouter(
    prefix="/chatbot",
    tags=["chatbot"],
)


@chatbot_router.get("")
async def ask_chatbot(
        question: str = Query(..., description="The question to ask the chatbot"),
):
    chatbot_service = ChatbotService()
    return chatbot_service.ask_question(question=question)
