from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from config import OPENAI_API_KEY

gpt_4o_model = ChatOpenAI(model_name="gpt-4o", api_key=OPENAI_API_KEY)


class ChatbotService:
    def __init__(self):
        self.prompting_techniques = {
            "zero_shot_prompting": """
                {question}
            """,
            "few_shot_prompting": """
                Here are some examples to guide you:
                Q: What is the capital of France? A: Paris
                Q: Who wrote 'Pride and Prejudice'? A: Jane Austen
                Q: {question}
                A:
            """,
            "chain_of_thought_prompting": """
                Let's break this down step by step:
                Q: {question}
                Step 1:
            """,
            "self_consistency_prompting": """
                Generate multiple reasoning paths for the following question and pick the most consistent answer:
                Q: {question}
            """,
            "tree_of_thoughts_prompting": """
                Solve this problem by exploring multiple possible solutions and refining the best branches:
                Q: {question}
                Start by outlining possible approaches.
            """,
            "directional_stimulus_prompting": """
                Answer the following question by explicitly directing focus and creativity:
                Stimulus: Think like a philosopher answering a profound question.
                Q: {question}
            """,
            "prompt_chaining_prompting": """
                Use the output of this question to inform the following step:
                Q1: What is the summary of this text? Answer: {answer1}
                Q2: Based on the summary, what is the central theme? Answer:
            """

        }

    def ask_question(self, question: str, prompt_technique: str, **kwargs):
        # Retrieve prompt template based on the selected mode
        prompt = self.prompting_techniques.get(prompt_technique, "zero_shot_prompting")
        prompt_template = PromptTemplate(template=prompt, input_variables=["question", *kwargs.keys()])

        # Build the chain
        chain = prompt_template | gpt_4o_model

        # Prepare arguments to pass into the prompt
        arguments = {"question": question, **kwargs}
        return chain.invoke(arguments)
