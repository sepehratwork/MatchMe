import json
from typing import Optional, Type

from langchain_core.tools import BaseTool
from typing_extensions import Annotated, TypedDict
from pydantic import BaseModel, Field

subjects = list(json.load(open("services/domains.json")).keys())


############## Greeting ##############
class GreetingInput(BaseModel):
    system_prompt: Optional[str] = Field(None, description="A system prompt for the guidance of how the LLM should work")
    user_prompt: Optional[list] = Field(None, description="User's chat")

class GreetingTool(BaseTool):
    name = "Greeting"
    description = "If the user's chat is just about greeting, this tool should be activated."
    args_schema: Type[BaseModel] = GreetingInput
    return_direct: bool = True

    def _run(
        self
    ) -> str:
        return "Greeting"


############## Introduction ##############
class IntroductionInput(BaseModel):
    system_prompt: Optional[str] = Field(None, description="A system prompt for the guidance of how the LLM should work")
    user_prompt: Optional[list] = Field(None, description="User's chat")

class IntroductionTool(BaseTool):
    name = "Introduction"
    description = "If the user's chat is about asking about the whole product's functionality or \
the user's chat is about what is this whole thing doing, then this tool should be activated."
    args_schema: Type[BaseModel] = IntroductionInput
    return_direct: bool = True

    def _run(
        self
    ) -> str:
        return "Introduction"


############## Irrelevant ##############
class IrrelevantInput(BaseModel):
    system_prompt: Optional[str] = Field(None, description="A system prompt for the guidance of how the LLM should work")
    user_prompt: Optional[list] = Field(None, description="User's chat")

class IrrelevantTool(BaseTool):
    name = "Irrelevant"
    subjects = list(json.load(open("services/domains.json")).keys())
    description = f"If the user's chat was not about greeting or asking about the whole's product functionality or any of the subjects given in the list: {subjects}, this tool should be activated."
    args_schema: Type[BaseModel] = IrrelevantInput
    return_direct: bool = True

    def _run(
        self
    ) -> str:
        return "Irrelevant"


############## Cancel ##############
class CancelInput(BaseModel):
    system_prompt: Optional[str] = Field(None, description="A system prompt for the guidance of how the LLM should work")
    user_prompt: Optional[list] = Field(None, description="User's chat")

class CancelTool(BaseTool):
    name = "Cancel"
    description = "Based on the user's chat, if the user wants to cancel the process in which the user is requesting for a service, this tool should be called."
    args_schema: Type[BaseModel] = CancelInput
    return_direct: bool = True

    def _run(
        self
    ) -> str:
        return "Cancel"


############## Relevant ##############
class RelevantInput(BaseModel):
    system_prompt: Optional[str] = Field(None, description="A system prompt for the guidance of how the LLM should work")
    user_prompt: Optional[list] = Field(None, description="User's chat")

class RelevantTool(BaseTool):
    name = "Relevant"
    subjects = list(json.load(open("services/domains.json")).keys())
    description = f"If the user's chat is about one of the subjects in the following list: {subjects}, then this tool should be used."
    args_schema: Type[BaseModel] = IrrelevantInput
    return_direct: bool = True

    def _run(
        self
    ) -> str:
        return "Relevant"
