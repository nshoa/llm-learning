from fastapi import APIRouter, HTTPException, Depends

from apps.chatbot.services.embedding_service import PDFEmbeddingService

chatbot_router = APIRouter(
    prefix="/chatbot",
    tags=["chatbot"],
)

from api.chatbot.schemas.user_question import UserQuestionSchema, RagUserQuestionSchema
from apps.chatbot.services.chatbot_service import ChatbotService

from langsmith import utils

utils.tracing_is_enabled()


@chatbot_router.get("/test_prompt")
async def ask_chatbot_test_prompt(
        user_question: UserQuestionSchema = Depends(),
):
    chatbot_service = ChatbotService()

    # Invoke the ChatbotService with question, mode, and extra arguments
    try:
        response = chatbot_service.ask_chatbot_test_prompt(**user_question.model_dump())
        return {
            "question": user_question.question,
            "response": response,
            "prompt_technique": user_question.prompt_technique
        }

    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while processing the request: {str(e)}"
        )


@chatbot_router.get("/test_rag")
async def ask_chatbot_test_rag(
        user_question: RagUserQuestionSchema = Depends(),
):
    try:
        # PDFEmbeddingService().get_embedding()
        chatbot_service = ChatbotService()
        response = chatbot_service.ask_chatbot_test_rag(**user_question.model_dump())
        return {
            "question": user_question.question,
            "response": response,
        }
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while processing the request: {str(e)}"
        )


@chatbot_router.post("/embedding_file")
def embedding_file():
    try:
        PDFEmbeddingService(file_name="Python_JD_PDF.pdf").get_embedding()
        return {"Embedding file successfully"}
    except Exception as e:
        print(e)
