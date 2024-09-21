from typing import Literal


def relevant_router(state) -> Literal["Greeting", "Introduction", "Irrelevant", "Cancel", "Relevant"]:
    reciever = state["reciever"]
    if reciever == "Greeting":
        return "Greeting"
    if reciever == "Introduction":
        return "Introduction"
    if reciever == "Irrelevant":
        return "Irrelevant"
    if reciever == "Cancel":
        return "Cancel"
    if reciever == "Relevant":
        return "Relevant"

def should_retrieve(state):
    if len(state["messages"]) > 6:
        return "yes"
    else:
        return "no"
