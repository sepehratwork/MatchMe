import json
from groq import Groq

from config import groq_api_key


client = Groq(api_key=groq_api_key)
domains = json.load(open("domain.json", "r"))

domain = "Shift dresses"
intent = "Buy"
for domain in domains.keys():
    for intent in domains[domain].keys():
        if domains[domain][intent] != [""]:
            continue
        else:
            print(f"Domain: {domain} - Intent: {intent}")
            prompt = f"""\
I want to have an AI assistant service based on RAG which maps a given sentence to a related domain and intent based on the examples existing in the vector database for that specific domain and intent. I want to solve this problem using few shot learning. There should be some examples for each of the domains and intents in the vector database and the metadata for each of the examples is their corresponding domain. This RAG should map the given input to the closest sentence so that the correct domain and intent would be found.
Now I will give you the domains and intents one by one and you should generate 30 examples which would cover all the different possibilities which that domain and intent would have when the user wants to select it. All the domains are about clothes and we want to find out that which kinds of clothes the user wants to Buy or Sell or just point to (None). Half of the examples should be for men and the women. The examples should cover all kinds of states and situations for buying or selling or just pointing to (None) that specific cloth.
You will be given a piece of cloth for whether buying or selling or just pointing to (None) and you should generate 30 examples with respect to the terms above.

Now with respect to the terms and conditions given above, generate 30 examples for domain {domain} and intent {intent}.
Only write the examples in your response and no other additional descriptions.
Generate your answer in a list format like the following:
["Example 1", "Example 2", ..., "Example 30"]\
"""
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": prompt
                    }
                ],
                temperature=1,
                # max_completion_tokens=1024,
                top_p=1,
                stream=False,
                stop=None,
            )
            answer = response.choices[0].message.content
            answer = answer.replace("\'", "")

            domains[domain][intent] = json.loads(answer)
            json.dump(domains, open("domain.json", "w"), indent=4, ensure_ascii=False)
