from groq import Groq

class ChatwithGroq:
    def __init__(self):
        self.client = Groq(api_key="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")
        self.model_name = "llama-3.1-70b-versatile"
        # self.model_name = "llama-3.1-8b-instant"
        # self.model_name = "llama-3.2-11b-vision-preview"
        self.temperature = 0
        self.max_tokens = 8000

    def choose_client(self):
        pass

    def create_messages(self, system_prompt, user_prompt, domain, intent, slots):
        if (not domain) and (not intent) and (not slots):
            self.messages = [
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ]

        elif domain and (not intent) and (not slots):
            self.messages = [
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "system",
                        "content": f"The user's specified domain is {domain}"
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ]

        elif domain and intent and (not slots):
            self.messages = [
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "system",
                        "content": f"The user's specified domain is {domain}"
                    },
                    {
                        "role": "system",
                        "content": f"The user's specified intent is {intent}"
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ]

        elif domain and intent and slots:
            self.messages = [
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "system",
                        "content": f"The user's specified domain is {domain}"
                    },
                    {
                        "role": "system",
                        "content": f"The user's specified intent is {intent}"
                    },
                    {
                        "role": "system",
                        "content": f"The user's specified slots is {slots}"
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ]

    def simple_answer(self, system_prompt, user_prompt, domain=None, intent=None, slots=None):
        self.create_messages(system_prompt, user_prompt, domain, intent, slots)
        completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=self.messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=1,
            stream=False,
            stop=None,
        )
        return completion.choices[0].message.content

    def streaming_answer(self, system_prompt, user_prompt, domain=None, intent=None):
        self.create_messages(system_prompt, user_prompt, domain, intent)
        completion = self.client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=self.messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=1,
            stream=True,
            stop=None,
        )
        for chunk in completion:
            yield chunk.choices[0].delta.content
