from utils import ChatwithGroq
from prompts import extract_domain_prompt, extract_intent_prompt, extract_slots_prompt

class MatchMe:
    def __init__(self):
        self.chat_with_groq = ChatwithGroq()

    def extract_domain(self, user_prompt):
        return self.chat_with_groq.simple_answer(extract_domain_prompt, user_prompt)

    def extract_intent(self, user_prompt, domain=None):
        return self.chat_with_groq.simple_answer(extract_intent_prompt, user_prompt, domain)

    def extract_slot(self, user_prompt, domain=None, intent=None):
        return self.chat_with_groq.simple_answer(extract_slots_prompt, user_prompt, domain, intent)

    # اره و انباری هم داشته باشه
    def extract_specific_slot_and_more(self, user_prompt, domain=None, intent=None, slots=None):
        return self.chat_with_groq.simple_answer(extract_slots_prompt, user_prompt, domain, intent, slots)
