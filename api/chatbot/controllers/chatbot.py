from fastapi import APIRouter, HTTPException, Depends

from api.chatbot.schemas.user_question import UserQuestionSchema
from apps.chatbot.services.chatbot_service import ChatbotService

chatbot_router = APIRouter(
    prefix="/chatbot",
    tags=["chatbot"],
)


@chatbot_router.get("")
async def ask_chatbot(
        user_question: UserQuestionSchema = Depends(),
):
    chatbot_service = ChatbotService()

    # Invoke the ChatbotService with question, mode, and extra arguments
    try:
        response = chatbot_service.ask_question(**user_question.model_dump())
        return {
            "question": user_question.question,
            "response": response,
            "prompt_technique": user_question.prompt_technique
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while processing the request: {str(e)}"
        )
