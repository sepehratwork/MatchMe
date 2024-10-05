from groq import Groq

class ChatwithGroq:
    def __init__(self):
        self.client = Groq(api_key="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")
        self.model_name = "llama-3.1-70b-versatile"
        self.temperature = 0
        self.max_tokens = 8000

    def choose_client(self):
        pass

    def simple_answer(self, system_prompt, user_prompt):
        completion = self.client.chat.completions.create(
            model=self.model_name,
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
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=1,
            stream=False,
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
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=1,
            stream=True,
            stop=None,
        )

        for chunk in completion:
            yield chunk.choices[0].delta.content
