from langchain import hub
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.constants import START
from langgraph.graph import StateGraph

from apps.utils.prompting_techniques import prompting_techniques
from apps.utils.state import State
from config import OPENAI_API_KEY
from core.common.constants import PromptTechnique
from core.common.vector_database import vector_store

gpt_4o_model = ChatOpenAI(model_name="gpt-4o", api_key=OPENAI_API_KEY)


class ChatbotService:
    def __init__(self):
        self.prompting_techniques: dict = prompting_techniques
        self.vector_store = vector_store

    def ask_chatbot_test_prompt(self, question: str, prompt_technique: str, **kwargs):
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

    def ask_chatbot_test_rag(self, question: str):
        graph = self.__build_graph()
        result = graph.invoke({"question": question})
        return result

    def __retrieve(self, state: State):
        retrieved_docs = self.vector_store.similarity_search(state["question"])
        return {"context": retrieved_docs}

    def __generate(self, state: State):
        # https://smith.langchain.com/hub/rlm/rag-prompt
        prompt = hub.pull("rlm/rag-prompt")

        docs_content = "\n\n".join(doc.page_content for doc in state["context"])
        messages = prompt.invoke({"question": state["question"], "context": docs_content})
        response = gpt_4o_model.invoke(messages)
        return {"answer": response.content}

    def __build_graph(self):
        graph_builder = StateGraph(State).add_sequence([self.__retrieve, self.__generate])
        graph_builder.add_edge(START, "__retrieve")
        graph = graph_builder.compile()
        return graph
