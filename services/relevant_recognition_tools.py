import json

from typing_extensions import Optional, ClassVar
from pydantic import BaseModel, Field

subjects = list(json.load(open("services/domains.json")).keys())


class Greeting(BaseModel):
    title: ClassVar = Field("Greeting")
    description: ClassVar = Field("""\
The Greeting tool is designed to be called whenever the user's input is primarily a greeting or salutation directed toward initiating friendly or polite interaction with the chatbot. 
This includes any message where the user expresses a standard greeting, acknowledges the chatbot's presence in a courteous manner, or engages in social pleasantries without requesting specific information or services.
The LLM should recognize and call the Greeting tool when the user's input consists of, but is not limited to, the following scenarios:

Standard Greetings:
Simple expressions like "Hello", "Hi", "Hey", "Good morning", "Good afternoon", "Good evening".
Friendly salutations such as "Greetings", "Howdy", "What's up", "Yo".

Polite Inquiries and Social Pleasantries:
Greetings combined with polite questions like "Hello, how are you?", "Hi there, how's it going?", "Hey, what's new?".
Expressions of well-wishing or courtesy, e.g., "Hope you're having a good day", "It's nice to chat with you", "Pleasure to meet you".

Informal and Colloquial Greetings:
Slang or colloquial terms used as greetings, such as "Heya", "Hiya", "Sup", "Yo buddy".
Regional or cultural greetings like "Namaste", "Hola", "Bonjour", "Ciao".

Greetings with Minor Typos or Variations:
Messages with minor spelling errors or abbreviations, e.g., "Helllo", "Hii", "G'day".

Guidelines for the LLM:
Primary Intent Focus: If the user's message is solely or primarily a greeting, the Greeting tool should be called.

Exclusions: Do not call the Greeting tool if the user's message contains:
Questions about services or functionalities.
Requests for assistance, information, or actions.
Statements unrelated to greetings, even if they start with a greeting.\
""")
    system_prompt: Optional[str] = Field(None, description="A system prompt for the guidance of how the LLM should work")
    user_prompt: Optional[list] = Field(None, description="User's chat")


class Introduction(BaseModel):
    title: ClassVar = Field("Introduction")
    description: ClassVar = Field("""\
The Introduction tool is designed to be called whenever the user's input indicates a desire to learn about the chatbot's capabilities, functionalities, services offered, or how to interact with it. 
This includes any message where the user is asking for an overview, instructions, or assistance in understanding what the chatbot can do for them.
The LLM should recognize and call the Introduction tool when the user's input consists of, but is not limited to, the following scenarios:

Direct Inquiries About Capabilities:
Questions like "What can you do?", "Tell me about your services.", "How can you help me?"
Requests for a list of functionalities, e.g., "What services do you offer?", "What are your features?"

Requests for Guidance on Usage:
Queries about how to interact with the chatbot, such as "How do I use this chatbot?", "Can you guide me through your functions?", "How does this work?"

Seeking Assistance or Help:
Statements indicating confusion or need for assistance, like "I need help understanding what you do.", "Can you explain how to use this service?", "I'm not sure how to proceed."

Inquiries About the Chatbot's Identity:
Questions about the chatbot itself, e.g., "Who are you?", "Are you a bot?", "What is your purpose?"

Exploratory Questions:
Open-ended requests for information, such as "Tell me about yourself.", "What can you assist me with?", "Give me an overview of your capabilities."

Guidelines for the LLM:
Primary Intent Focus: If the user's message is primarily about learning the capabilities or functionalities of the chatbot, the Introduction tool should be called.\
""")
    system_prompt: Optional[str] = Field(None, description="A system prompt for the guidance of how the LLM should work")
    user_prompt: Optional[list] = Field(None, description="User's chat")


class Irrelevant(BaseModel):
    title: ClassVar = Field("Irrelevant")
    description: ClassVar = Field(f"""\
The Irrelevant tool is designed to be called whenever the user's input is not related to the services, capabilities, or functionalities that the chatbot provides.
This includes any message where the user discusses topics, asks questions, or makes statements that fall outside the scope of the chatbot's domain. 
The primary purpose of this tool is to identify and handle inputs that are beyond the chatbot's expertise or service offerings, ensuring efficient and relevant interactions.
Here is the list of services which the chatbot can recieve request for: {subjects}
The LLM should recognize and call the Irrelevant tool when the user's input consists of, but is not limited to, the following scenarios:

Unrelated Topics:
Questions or discussions about subjects not covered by the chatbot, such as weather, sports, news, general knowledge, entertainment, or personal opinions.
Inquiries like "What's the capital of France?", "Who won the soccer match last night?", "Tell me a joke."

Personal Inquiries About the Chatbot:
Questions about the chatbot's personal preferences or characteristics, e.g., "What's your favorite movie?", "Do you like music?", "How old are you?"

Technical Support for Unrelated Services:
Requests for help with products or services not offered by the chatbot, such as "My phone isn't working, can you fix it?", "How do I reset my email password?"

Random or Off-Topic Statements:
Comments that are not seeking assistance or information related to the chatbot's services, like "I love pizza.", "It's raining outside.", "I'm feeling happy today."

Inappropriate or Prohibited Content:
Messages containing offensive language, hate speech, harassment, or any content that violates community guidelines.

General Knowledge Questions:
Queries seeking information that is not within the chatbot's domain, such as "Explain quantum physics.", "How do airplanes fly?", "What is the meaning of life?"

Guidelines for the LLM:
Primary Intent Focus: If the user's message is mainly about a topic outside the chatbot's services, the Irrelevant tool should be called.\
""")
    system_prompt: Optional[str] = Field(None, description="A system prompt for the guidance of how the LLM should work")
    user_prompt: Optional[list] = Field(None, description="User's chat")


class Cancel(BaseModel):
    title: ClassVar = Field("""\
The Cancel tool is designed to be called whenever the user expresses a desire to terminate, exit, or withdraw from an ongoing process related to the services provided by the chatbot.
This includes any message where the user indicates that they no longer wish to continue with a service request, appointment, transaction, or any interaction that is part of the chatbot's domain.
The primary purpose of this tool is to acknowledge the user's intent to cancel and to take appropriate action to cease the current process, ensuring that the user's wishes are respected promptly and accurately.

The LLM should recognize and call the Cancel tool when the user's input consists of, but is not limited to, the following scenarios:

Explicit Cancellation Requests:
Direct statements like "Cancel my request," "I want to cancel," "Please stop this process," "Forget about it," "Disregard my last message."

Withdrawal from a Service or Action:
Indications that the user no longer wants to proceed, such as "I changed my mind," "I'm no longer interested," "Let's not proceed," "I don't want to continue."

Cancellation of Appointments or Bookings:
Requests to cancel scheduled events, e.g., "Cancel my viewing appointment," "I need to cancel my booking," "Please cancel my reservation."

Termination of Interaction:
Statements expressing the desire to end the conversation or interaction, like "I'm done," "That's all, thank you," "I wish to end this chat."

Expressions of Frustration Leading to Cancellation:
Messages indicating frustration or dissatisfaction leading to cancellation, e.g., "This is taking too long, cancel it," "Forget it, I'll do it later," "This isn't working, please cancel."

Guidelines for the LLM:
Primary Intent Focus: If the user's message clearly indicates a wish to cancel or terminate a service-related process, the Cancel tool should be called.
Combined Messages: If a message includes a cancellation along with other intents, prioritize the Cancel tool if the cancellation is the primary intent. For example, "Cancel my appointment and tell me about your services" would require assessing which intent is primary.
Exclusions: Do not call the Cancel tool if the user's message is:
A general inquiry about services (should trigger the Relevant tool).
A greeting or salutation without any cancellation intent (should trigger the Greeting tool).
An inquiry about the chatbot's capabilities or how to use it without any cancellation intent (should trigger the Introduction tool).
Unrelated to the chatbot's services or domain (should trigger the Irrelevant tool).
""")
    description: ClassVar = Field("""
The user is going through a process throughout their chat. Now, they want to fall back and exit the on going process.
This is the time when this tool must be called.
""")
    system_prompt: Optional[str] = Field(None, description="A system prompt for the guidance of how the LLM should work")
    user_prompt: Optional[list] = Field(None, description="User's chat")


class Relevant(BaseModel):
    title: ClassVar = Field("Relevant")
    description: ClassVar = Field(f"""\
The Relevant tool is designed to be called whenever the user's input pertains directly to the services, capabilities, or functionalities that the chatbot provides. 
This includes any message where the user is requesting assistance, information, or action related to the services offered by the chatbot.
The primary purpose of this tool is to facilitate user requests that fall within the chatbot's domain, ensuring that users receive accurate and helpful responses to their inquiries or service needs.
Here is the list of services which the chatbot can recieve request for: {subjects}

The LLM should recognize and call the Relevant tool when the user's input consists of, but is not limited to, the following scenarios:
Service Requests:
Direct inquiries or requests for specific services provided by the chatbot, such as "I want to rent an apartment," "Help me find a house," "I need a property to buy."
Expressions of intent to use a service, e.g., "I'm looking for office space," "I need to schedule a viewing for a rental property."

Information Seeking Within Domain:
Questions seeking details about specific services, like "What properties are available in downtown?" "Do you have any 2-bedroom apartments?"
Inquiries about availability, pricing, features, or specifications of services offered.

Action-Oriented Requests:
Requests to perform actions related to services, such as "Book an appointment with a real estate agent," "Schedule a property tour," "Submit an application for a rental."

Service-Related Problem Solving:
Issues or problems the user is facing within the scope of services, e.g., "I'm having trouble accessing my account," "I can't find listings in my area," "My application was rejected, can you help?"

Follow-Up on Previous Interactions:
References to earlier conversations or actions, like "About the apartment we discussed," "Can we continue where we left off?" "Any updates on my rental application?"

Customization and Preferences:
Requests to tailor services to user preferences, such as "I'm looking for a pet-friendly apartment," "Show me properties under $1,500 per month," "I prefer houses with a garden."

Guidelines for the LLM:
Primary Intent Focus: If the user's message is primarily about obtaining services, assistance, or information that the chatbot provides, the Relevant tool should be called.
Exclusions: Do not call the Relevant tool if the user's message is:
A greeting or salutation without a service request (should trigger the Greeting tool).
An inquiry about the chatbot's capabilities or how to use it without a specific service request (should trigger the Introduction tool).
A request to cancel a service or process (should trigger the Cancel tool).
Unrelated to the chatbot's services or domain (should trigger the Irrelevant tool).\
""")
    system_prompt: Optional[str] = Field(None, description="A system prompt for the guidance of how the LLM should work")
    user_prompt: Optional[list] = Field(None, description="User's chat")
