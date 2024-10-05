from utils import ChatwithGroq
from prompts import *

class MatchMe:
    def __init__(self):
        self.chat_with_groq = ChatwithGroq()

    def extract_domain(self, user_prompt):
        return self.chat_with_groq.simple_answer(extract_domain_prompt, user_prompt)

    def extract_entity(self, user_prompt):
        return self.chat_with_groq.simple_answer(extract_domain_prompt, user_prompt)

    def extract_slot(self, user_prompt):
        return self.chat_with_groq.simple_answer(extract_domain_prompt, user_prompt)
