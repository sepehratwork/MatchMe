from groq import Groq

class ChatwithGroq:
    def __init__(self):
        self.client = Groq(api_key="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")

    def choose_client(self):
        pass

    def simple_answer(self, system_prompt, user_prompt):
        completion = self.client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            temperature=0,
            max_tokens=8196,
            top_p=1,
            stream=True,
            stop=None,
        )
        return completion.choices[0].message.content

    def streaming_answer(self, system_prompt):
        completion = self.client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": ""
                }
            ],
            temperature=0,
            max_tokens=8196,
            top_p=1,
            stream=True,
            stop=None,
        )

        for chunk in completion:
            yield chunk.choices[0].delta.content
