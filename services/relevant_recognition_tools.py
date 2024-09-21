import json

from typing_extensions import Optional, ClassVar
from pydantic import BaseModel, Field

subjects = list(json.load(open("services/domains.json")).keys())


class Greeting(BaseModel):
    title: ClassVar = Field("Greeting")
    description: ClassVar = Field("")
    system_prompt: Optional[str] = Field(None, description="A system prompt for the guidance of how the LLM should work")
    user_prompt: Optional[list] = Field(None, description="User's chat")


class Introduction(BaseModel):
    title: ClassVar = Field("Introduction")
    description: ClassVar = Field("")
    system_prompt: Optional[str] = Field(None, description="A system prompt for the guidance of how the LLM should work")
    user_prompt: Optional[list] = Field(None, description="User's chat")


class Irrelevant(BaseModel):
    title: ClassVar = Field("Irrelevant")
    description: ClassVar = Field("")
    system_prompt: Optional[str] = Field(None, description="A system prompt for the guidance of how the LLM should work")
    user_prompt: Optional[list] = Field(None, description="User's chat")


class Cancel(BaseModel):
    title: ClassVar = Field("Cancel")
    description: ClassVar = Field("")
    system_prompt: Optional[str] = Field(None, description="A system prompt for the guidance of how the LLM should work")
    user_prompt: Optional[list] = Field(None, description="User's chat")


class Relevant(BaseModel):
    title: ClassVar = Field("Relevant")
    description: ClassVar = Field("")
    system_prompt: Optional[str] = Field(None, description="A system prompt for the guidance of how the LLM should work")
    user_prompt: Optional[list] = Field(None, description="User's chat")
