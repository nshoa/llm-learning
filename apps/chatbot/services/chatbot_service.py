from langchain_core.messages import SystemMessage
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START
from langgraph.graph import StateGraph, MessagesState
from langgraph.prebuilt import tools_condition

from apps.chatbot.common.constants import PromptTechnique
from apps.chatbot.common.prompting_techniques import prompting_techniques
from apps.chatbot.utils.chatbot_tools import retrieve_from_database, tools
from config import OPENAI_API_KEY
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
        # result = graph.invoke({"messages": [{"role": "user", "content": question}]})

        # Specify an ID for the thread (chat history)
        config = {"configurable": {"thread_id": "abc123"}}

        result = graph.stream(
            {"messages": [{"role": "user", "content": question}]},
            stream_mode="values",
            config=config
        )
        for value in result:
            value["messages"][-1].pretty_print()

        # result = graph.stream(
        #     {"messages": [
        #         {"role": "user", "content": "What benefits does that job offer?"}]},
        #     stream_mode="values",
        #     config=config
        # )
        # for value in result:
        #     value["messages"][-1].pretty_print()

        return result

    def __query_or_respond(self, state: MessagesState):
        """Generate tool call for retrieve or respond"""
        llm_model_with_tool = gpt_4o_model.bind_tools([retrieve_from_database])
        response = llm_model_with_tool.invoke(state["messages"])
        return {"messages": [response]}

    def __generate(self, state: MessagesState):
        """Generate answer."""
        # Get generated tool messages
        recent_tool_messages = []
        for message in reversed(state["messages"]):
            if message.type == "tool":
                recent_tool_messages.append(message)
            else:
                break

        tool_messages = recent_tool_messages[::-1]
        docs_content = "\n\n".join(doc.content for doc in tool_messages)
        system_message_content = (
            "You are an assistant for question-answering tasks. "
            "Use the following pieces of retrieved context to answer "
            "the question. If you don't know the answer, say that you "
            "don't know. Use three sentences maximum and keep the "
            "answer concise."
            "\n\n"
            f"{docs_content}"
        )

        conversation_messages = [
            message
            for message in state["messages"]
            if message.type in ("human", "system") or (message.type == "ai" and not message.tool_calls)
        ]

        prompt = [SystemMessage(system_message_content)] + conversation_messages
        response = gpt_4o_model.invoke(prompt)

        return {"messages": [response]}

    def __build_graph(self):
        graph_builder = StateGraph(MessagesState)

        # Add nodes
        graph_builder.add_node(self.__query_or_respond)
        graph_builder.add_node(tools)
        graph_builder.add_node(self.__generate)

        # Add edges
        graph_builder.add_edge(START, "__query_or_respond")
        graph_builder.add_conditional_edges(
            "__query_or_respond",
            tools_condition,
            {END: END, "tools": "tools"}
        )
        graph_builder.add_edge("tools", "__generate")
        graph_builder.add_edge("__generate", END)

        # Memory checkpointer - for chat history
        memory = MemorySaver()

        graph = graph_builder.compile(checkpointer=memory)

        return graph

    # def __draw_graph_image(self, graph):
    #     graph_image = graph.get_graph().draw_mermaid_png()
    #     with open("graph_visualization/rag_with_tools.png", "wb") as f:
    #         f.write(graph_image)
