from fastapi import APIRouter, Query, HTTPException

from apps.chatbot.services import ChatbotService

chatbot_router = APIRouter(
    prefix="/chatbot",
    tags=["chatbot"],
)


@chatbot_router.get("")
async def ask_chatbot(
        question: str = Query(..., description="The question to ask the chatbot"),
        prompt_technique: str = Query(
            "zero_shot_prompting",
            description="The prompting technique to use. Options: zero_shot_prompting, few_shot_prompting, chain_of_thought_prompting, self_consistency_prompting, tree_of_thoughts_prompting, directional_stimulus_prompting, prompt_chaining_prompting"
        ),
):
    chatbot_service = ChatbotService()

    # Invoke the ChatbotService with question, mode, and extra arguments
    try:
        response = chatbot_service.ask_question(question=question, prompt_technique=prompt_technique)
        return {"question": question, "response": response, "prompt_technique": prompt_technique}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while processing the request: {str(e)}"
        )