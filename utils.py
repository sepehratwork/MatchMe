import os
import json

from langchain_groq import ChatGroq
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import FunctionMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from services.relevant_recognition_tools import Greeting, Introduction, Irrelevant, Cancel, Relevant


class Utils:
    def __init__(self):
        self.tool_calling_llm = ChatGroq(
            model=os.getenv("groq_model_name_1"),
            temperature=0,
        )
        self.chatting_llm = ChatGroq(
            model=os.getenv("groq_model_name_2"),
            temperature=0.2,
        )
        self.gpt = AzureChatOpenAI(
            # model = "gpt_4_32k",
            model = "gpt-4o",
            api_key = "4a342430ad17498da149a9b77bf4c51f",
            api_version = "2023-10-01-preview",
            azure_endpoint = "https://tensurfbrain.openai.azure.com/",
            temperature = 0,
            streaming = False
        )
        self.chat_history_len = 1

    # TODO changing elements of the json into corresponding langchain message objects
    def chat_history_management(self, state):
        chat_history = clean_messages(state["messages"])[-self.chat_history_len:]
        return {
            "chat_history": chat_history
        }

    # TODO managing chat histry using retriever
    def adding_retriever(self, state):
        retrieved_histor = state["messages"][:-self.chat_history_len]

    def relevant_detection_node(self, state):
        tools = [Greeting, Introduction, Irrelevant, Cancel, Relevant]
        llm_with_tools = self.chatting_llm.bind_tools(tools)
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    # TODO modifying prompt engineering
                    "You are a helpful AI assistant, collaborating with other assistants."
                    " Use the provided tools to progress towards answering the question."
                    " Given the chat history of the user, you must choose between the tools you have access to with respect to the given content."
                    " You have access to the following tools: {tool_names}.",
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )
        prompt = prompt.partial(tool_names=", ".join([tool.title.default for tool in tools]))
        chain = prompt | llm_with_tools
        response = chain.invoke(state)
        return {
            "reciever": [dict(response)["additional_kwargs"]["tool_calls"][-1]["function"]["name"]]
        }

    def greeting(self, state):
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful and kindful assistant. The user wants to greet with you. Just answer their greetings kindly.",
                ),
                MessagesPlaceholder("messages")
            ]
        )
        chain = prompt | self.chatting_llm
        response = chain.invoke(state)
        response = FunctionMessage(content=response.content, name="Greeting")
        return {
            "messages": [response],
        }

    def introduction(self, state):
        subjects = list(json.load(open("services/domains.json")).keys())
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful and kindful assistant. The user is asking about your capabilities and functionalities. Your job as an asistant is to match clients and businesses together in these fields: {subjects}. With these given information introduce yourself to the user.",
                ),
                MessagesPlaceholder("messages")
            ]
        )
        prompt = prompt.partial(subjects=", ".join([subject for subject in subjects]))
        chain = prompt | self.chatting_llm
        response = chain.invoke(state)
        response = FunctionMessage(content=response.content, name="Introduction")
        return {
            "messages": [response],
        }

    def irrelevant(self, state):
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful and kindful assistant. The user have demanded for something which is beyond our capabilities. Politely tell them that you can not help them.",
                ),
                MessagesPlaceholder("messages")
            ]
        )
        chain = prompt | self.chatting_llm
        response = chain.invoke(state)
        response = FunctionMessage(content=response.content, name="Irrelevant")
        return {
            "messages": [response],
        }

    # TODO completing the jobs which need to be done in cancel mode
    def cancel(self, state):
        return {
            "cancel": True,
        }

    # TODO generating the wanted JSON + chatting with user + removing the vector database files + adding the response to the messages
    def generate_output(self, state):
        last_message = state["messages"][-1]
        domain = state["reciever"][-1].content
        message = last_message.content
        return{
            "messages": [AIMessage(content=message, name=domain)],
            "output_json": {"domain": domain, "message": message},
        }


# TODO cleaning the messages from the additional ones
def clean_messages(messages):
        cleaned_messages = []
        for message in messages:
            if (message.content != "") and (not isinstance(message, FunctionMessage)):
                cleaned_messages.append(message)
        return cleaned_messages
