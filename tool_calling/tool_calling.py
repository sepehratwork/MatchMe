import time
from groq import Groq

from tools import tools


def main(user_input: str):
    client = Groq(
        # api_key="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",
        )
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant, collaborating with other assistants."
                    " Use the provided tools to progress towards answering the question."
                    " Given the chat history of the user, you must choose between the tools you have access to with respect to the given content."
                    " You have access to the following tools: [Greeting, Introduction, Irrelevant, Cancel, Relevant].",
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=0,
        # max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
        # tools=tools,
        functions=tools,
        function_call="required"
    )

    return completion.choices[0].message.function_call.name


sample_prompts_relevance = {
    
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
    [
        "Find an apartment for rent.",
        "How much rent should I pay in avarage to live in tehran?",
        "I want to order a pizza.",
        "I have a stomachache. I need to see a doctor.",
        "Buy me a train ticket.",
    ]
}


for subject in sample_prompts_relevance:
    print(f"\nSubject:  {subject}")
    prompts = sample_prompts_relevance[subject]
    num_correct = 0
    for prompt in prompts:
        start = time.time()
        results = main(user_input=prompt)
        end = time.time()
        if results == subject:
            num_correct += 1
        print(f"Prompt: {prompt}\nAnswer: {results}\nInference: {round(end-start, 2)}\n")
        time.sleep(1)
    print(f"The result of the test of subject {subject}:  {num_correct}/{len(prompts)}\n\n")
