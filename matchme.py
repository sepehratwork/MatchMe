from typing import TypedDict, Annotated

from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

import routers
from utils import Utils
from services import domains
# from database.checkpoint import MongoDBSaver, MongoClient


class MatchMe:
    def __init__(self, user_id, chat_session):
        # setting a mongodb session for the user
        # MONGO_URI = "mongodb://localhost:27017/"
        # self.checkpointer = MongoDBSaver(MongoClient(MONGO_URI), f"{user_id}")
        self.config = {"configurable": {"thread_id": f"{chat_session}"}}
        self.dom = domains.Domains()
        domain_tools, vector_store = self.dom.create_domains()
        self.domains = ToolNode(tools=domain_tools)
        self.utils = Utils()

    def create_graph(self):
        builder = StateGraph(State)

        # defining nodes
        builder.add_node("Chat History Management", self.utils.chat_history_management)
        builder.add_node("Adding Retriever", self.utils.adding_retriever)
        builder.add_node("Relevent Detection", self.utils.relevant_detection_node)
        builder.add_node("Greeting", self.utils.greeting)
        builder.add_node("Introduction", self.utils.introduction)
        builder.add_node("Irrelevant", self.utils.irrelevant)
        builder.add_node("Cancel", self.utils.cancel)
        builder.add_node("Select Domains", self.dom.domain_select_tools)
        builder.add_node("Domain Agent", self.dom.create_domain_agent)
        builder.add_node("Domains", self.domains)
        builder.add_node("Output Generation", self.utils.generate_output)

        # defining start and finish points
        builder.set_entry_point("Chat History Management")
        builder.set_finish_point("Output Generation")

        # defining edges
        builder.add_edge("Adding Retriever", "Relevent Detection")
        builder.add_edge("Greeting", "Output Generation")
        builder.add_edge("Introduction", "Output Generation")
        builder.add_edge("Irrelevant", "Output Generation")
        builder.add_edge("Cancel", "Output Generation")
        builder.add_edge("Domains", "Select Domains")
        builder.add_edge("Select Domains", "Domain Agent")
        builder.add_conditional_edges(
            "Chat History Management",
            routers.should_retrieve,
            {"yes": "Adding Retriever", "no": "Relevent Detection"}
        )
        builder.add_conditional_edges(
            "Relevent Detection",
            routers.relevant_router,
            {
                "Greeting": "Greeting", 
                "Introduction": "Introduction", 
                "Irrelevant": "Irrelevant",
                "Cancel": "Cancel",
                "Relevant": "Select Domains", 
            }
        )
        builder.add_conditional_edges(
            "Domain Agent",
            tools_condition,
            {"tools": "Domains", "__end__": "Output Generation"}
        )

        graph = builder.compile()
        
        return graph


class State(TypedDict):
    messages: Annotated[list, add_messages]
    chat_history: list
    selected_tools: list[str]
    output_json: dict
    reciever: Annotated[list[str], add_messages]
    cancel: bool
