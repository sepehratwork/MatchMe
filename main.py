from dotenv import load_dotenv

from langchain_core.messages import HumanMessage

from matchme import MatchMe

load_dotenv()


class Main:
    def __init__(self, user_id, chat_session):
        self.matchme = MatchMe(user_id, chat_session)
        self.graph = self.matchme.create_graph()

    def run(self, user_prompt):

        # TODO forcing function calling for relevant in relevant detection node
        input_json = {
                "messages": [
                    HumanMessage(content=user_prompt),
                ],
            }
        results = self.graph.invoke(
            input_json, 
            config=self.matchme.config, 
            stream_mode="updates",
            )

        return results

