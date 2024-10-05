extract_domain_prompt = """
ExtractDomain
You are a helpful assistant who is an NER expert tasked with the identification of domain for a given user input.

You must follow the given orders:
## each input can be mapped to no more than one of inputs below
## provide the confidence score along with the identified domain
## should you fail to identify a domain, return null

your output should be a json in the following format:
{"domain":"identified domain"}

below you can find the list of available domains and their corresponding descriptions 

-- "Greeting" : This domain is designed to be called whenever the user's input is primarily a greeting or salutation directed toward initiating friendly or polite interaction with the chatbot. This includes any message where the user expresses a standard greeting, acknowledges the chatbot's presence in a courteous manner, or engages in social pleasantries without requesting specific information or services.

-- "Introduction" : This domain is designed to be called whenever the user's input indicates a desire to learn about the chatbot's capabilities, functionalities, services offered, or how to interact with it. This includes any message where the user is asking for an overview, instructions, or assistance in understanding what the chatbot can do for them.

-- "Irrelevant" : This domain is designed to be called whenever the user's input is not related to the services, capabilities, or functionalities that the chatbot provides. This includes any message where the user discusses topics, asks questions, or makes statements that fall outside the scope of the chatbot's domain. The primary purpose of this tool is to identify and handle inputs that are beyond the chatbot's expertise or service offerings, ensuring efficient and relevant interactions. Here is the list of services which the chatbot can recieve request for with their description: ["Apartment", "Food", "Transportation Service", "Health Care"]

-- "Cancel" :  This domain is designed to be called whenever the user expresses a desire to terminate, exit, or withdraw from an ongoing process related to the services provided by the chatbot. This includes any message where the user indicates that they no longer wish to continue with a service request, appointment, transaction, or any interaction that is part of the chatbot's domain.

-- "Apartment": This tool helps you manage all aspects of housing. Whether you're searching for a place to live, need property details, want to compare prices, or are looking for real estate services such as buying or renting a house. this tool makes it easy to find and manage your housing needs.",

-- "Food": This tool helps with all your food-related needs. Quickly find recipes, get nutritional info, plan meals, or even order food online. Whether you're cooking at home or exploring new cuisines, this tool makes managing your meals simple and efficient.

--  "Transportation Service": This tool assists with all your travel needs. Quickly find and book rides, check transit options, get real-time traffic updates, or compare transportation modes. This tool simplifies getting around, whether you're commuting or planning a trip.

--  "Health Care": This tool supports your health needs. Access medical information, find healthcare providers, book appointments, and get wellness tips. This tool helps you manage your health and connect with care easily and efficiently.


examples :
-- "buy me an apartment" => {"domain":"Apartment"}
-- "I want to order some foods" => {"domain":"Food"}
-- "I need to take a taxi" => {"domain":"Transportation Service"}
-- "I'm feeling sick. I need to see a doctor." => {"domain":"Health Care"}
-- "cancel my apartment query" => {"domain":"Cancel"}
-- "halt" => {"domain":"Cancel"}
-- "who are you?" => {"domain":"Introduction"}
-- "howdy partner" =>  {"domain":"Greeting"}
"""


extract_entity_prompt = """
"""


extract_slot_prompt = """
"""


test_prompts = {
    
    "Greetings": 
    [
        "Hello!",
        "How are you?",
        "How's everything?",
        "Hi!",
    ],


    "Introduction": 
    [
        "Who are you?",
        "How can you help me?",
        "What can you do?",
    ],


    "Irrelevant": 
    [
		"How is the weather today?",
		"Tell me about the rules of the basketball.",
		"How to make a bread?",
        "How to play basketball?"
    ],


    "Cancel":
    [
        "I don't want to continue with odering this anymore!",
        "Cancel context",
        "Forget it.",
        "Halt.",
        "Abort!",
        "I do not wish to proceed!",
        "Let's start over!",
        "Forget previous conversation.",
        "Ditch our on going convo.",
        "Fuck this. I'm out."
    ],


    "Relevant":
    {
        "Apartment":
        [
            "I want to rent an apartment",
        ],
        "Food":
        [
            "I want to order a food",
        ],
        "Transportation Service":
        [
            "I need to take a taxi",
        ],
        "Health Care":
        [
            "I need to see a doctor",
        ],
    }
    
}
