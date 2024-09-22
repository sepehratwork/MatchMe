import json

from typing_extensions import Optional, ClassVar
from pydantic import BaseModel, Field

subjects = list(json.load(open("services/domains.json")).keys())


class Greeting(BaseModel):
    title: ClassVar = Field("Greeting")
    description: ClassVar = Field("""his tool is designed to handle user-initiated greetings within a conversation. When the user provides input that matches typical greeting phrases (e.g., "hi," "how are you," "hello"), the tool responds appropriately by acknowledging the greeting in a friendly manner. The tool is only called when the user's input is identified as a greeting, helping to create a natural and conversational interaction.

This tool enables the LLM to:

Recognize and respond to greetings.
Engage in polite conversational openers.
Ensure a friendly and welcoming tone when starting or maintaining a conversation.
The expected usage is when the user begins interaction with phrases like:

"- hi"
"- hello"
"- how are you?"
"- what's up?"
When invoked, the tool provides a warm and relevant response that keeps the conversation flowing naturally.""")
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
    description: ClassVar = Field("""
The user is going through a process throughout their chat. Now, they want to fall back and exit the on going process.
This is the time when this tool must be called.
""")
    system_prompt: Optional[str] = Field(None, description="A system prompt for the guidance of how the LLM should work")
    user_prompt: Optional[list] = Field(None, description="User's chat")


class Relevant(BaseModel):
    title: ClassVar = Field("Relevant")
    description: ClassVar = Field("")
    system_prompt: Optional[str] = Field(None, description="A system prompt for the guidance of how the LLM should work")
    user_prompt: Optional[list] = Field(None, description="User's chat")
