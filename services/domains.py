import os
import re
import uuid
import json

from langchain_groq import ChatGroq
from langchain_core.documents import Document
from langchain_core.tools import StructuredTool
from langchain_openai import AzureOpenAIEmbeddings
from pydantic import BaseModel, Field
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage

# from utils import clean_messages


class Domains:
    def __init__(self):
        self.embedding_model = AzureOpenAIEmbeddings(deployment="embedding-ada-002",
                                                model= "text-embedding-ada-002",
                                                azure_endpoint="https://tensurfbrain1.openai.azure.com/",
                                                openai_api_type="azure",
                                                chunk_size=1e9)
        self.domains = json.load(open("services/domains.json", "r"))
        self.domain_tool_registry = {
            str(uuid.uuid4()): self.create_domain_tool(domain) for domain in self.domains.keys()
        }
        self.llm = ChatGroq(
            model=os.getenv("groq_model_name_1"),
            temperature=0,
        )
        self.vector_store = InMemoryVectorStore(embedding=self.embedding_model)

    def create_domain_tool(self, domain: str) -> dict:
        formatted_domain = re.sub(r"[^\w\s]", "", domain).replace(" ", "_")

        def domain_tool() -> str:
            return f"{domain}"

        return StructuredTool.from_function(
            domain_tool,
            name=formatted_domain,
            description=self.domains[domain],
        )

    def create_domains(self):
        domains = [
            Document(
                page_content=tool.description,
                id=id,
                metadata={"tool_name": tool.name},
            )
            for id, tool in self.domain_tool_registry.items()
        ]
        document_ids = self.vector_store.add_documents(domains)
        domains = list(self.domain_tool_registry.values())
        return domains, self.vector_store
    
    def create_domain_agent(self, state):
        selected_tools = [self.domain_tool_registry[id] for id in state["selected_tools"]]
        llm_with_tools = self.llm.bind_tools(selected_tools)
        return {"messages": [llm_with_tools.invoke(state["messages"])]}

    # TODO deciding whether cleaning messages should be done or not
    def domain_select_tools(self, state):
        last_message = state["messages"][-1]
        hack_remove_tool_condition = False
        if isinstance(last_message, HumanMessage):
            query = last_message.content
            hack_remove_tool_condition = True
        else:
            assert isinstance(last_message, ToolMessage)
            system = SystemMessage(
                "Given this conversation, generate a query for additional tools. "
                "The query should be a short string containing what type of information "
                "is needed. If no further information is needed, "
                "set more_information_needed False and populate a blank string for the query."
            )
            input_messages = [system] + state["messages"]
            response = self.llm.bind_tools(
                [QueryForTools], tool_choice=True
            ).invoke(input_messages)
            query = response.tool_calls[0]["args"]["query"]
        tool_documents = self.vector_store.similarity_search(query)
        if hack_remove_tool_condition:
            # Remove needed tool
            selected_tools = [
                document.id
                for document in tool_documents
                if document.metadata["tool_name"] != "Advanced_Micro_Devices"
            ]
        else:
            selected_tools = [document.id for document in tool_documents]
        return {"selected_tools": selected_tools}


class QueryForTools(BaseModel):
    """Generate a query for additional tools."""
    query: str = Field(..., description="Query for additional tools.")
