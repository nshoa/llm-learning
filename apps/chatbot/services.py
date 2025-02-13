from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from config import OPENAI_API_KEY

gpt_4o_model = ChatOpenAI(model_name="gpt-4o", api_key=OPENAI_API_KEY)


class ChatbotService:
    def ask_question(self, question: str):
        prompt = """
            Answer this question: {question}
        """
        prompt_template = PromptTemplate(template=prompt, input_variables=["question"])

        chain = prompt_template | gpt_4o_model
        return chain.invoke({"question": question})
