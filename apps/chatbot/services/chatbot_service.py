from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from apps.utils.prompting_techniques import prompting_techniques
from config import OPENAI_API_KEY
from core.common.constants import PromptTechnique

gpt_4o_model = ChatOpenAI(model_name="gpt-4o", api_key=OPENAI_API_KEY)


class ChatbotService:
    def __init__(self):
        self.prompting_techniques: dict = prompting_techniques

    def ask_question(self, question: str, prompt_technique: str, **kwargs):
        # Retrieve prompt template based on the selected mode
        prompt = self.prompting_techniques.get(
            prompt_technique, self.prompting_techniques[PromptTechnique.zero_shot_prompting]
        )
        prompt_template = PromptTemplate(template=prompt, input_variables=["question", *kwargs.keys()])

        # Build the chain
        chain = prompt_template | gpt_4o_model

        # Prepare arguments to pass into the prompt
        arguments = {"question": question, **kwargs}
        return chain.invoke(arguments)
