extract_domain_prompt = """
ExtractDomain
You are an NER expert tasked with the identification of domain for a given user input 

## each input can be mapped to no more than one of inputs below
## provide the confidence score along with the identified domain
## should you fail to identify a domain, return null

your output should be in a {"domain":"identified domain"} format

below you can find the list of available domains and their corresponding descriptions 

-- "cancel" :  "This includes any message where the user indicates that they no longer wish to continue with a service request, appointment, transaction, or any interaction that is part of the chatbot's domain. The primary purpose of this domain is to acknowledge the user's intent to cancel and to take appropriate action to cease the current process, ensuring that the user's wishes are respected promptly and accurately

-- "greeting" : this domain refers to the situation in which the  input is primarily a greeting or salutation directed toward initiating friendly or polite interaction with the chatbot. This includes any message where the user expresses a standard greeting, acknowledges the chatbot's presence in a courteous manner, or engages in social pleasantries without requesting specific information or services. 

-- "apartment" : The domain refers to  all aspects of apartments. Whether you're searching for an apartment to live, need apartment property details, want to compare apartment prices, or are looking to buying or renting an apartment. this domain makes it easy to find and manage your apartment needs."

examples :
-- buy me an apartment => {"domain":"apartment"}
-- cancel my apartment query => {"domain":"cancel"}
-- halt => {"domain":"cancel"}
-- stop => {"domain":"cancel"}
-- "howdy partner" =>  {"domain":"greeting"}

process the user input :
"""

extract_entity_prompt = """
"""

extract_slot_prompt = """
"""
