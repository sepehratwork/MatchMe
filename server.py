from langdetect import detect
from concurrent import futures
import grpc
import MatchHub_pb2
import MatchHub_pb2_grpc

from main import Extractor
extractor_en = Extractor(model_name="sentence-transformers/all-mpnet-base-v2", v_db="domain_intent_en")
extractor_fa = Extractor(model_name="heydariAI/persian-embeddings", v_db="domain_intent_fa")

class MessageService(MatchHub_pb2_grpc.MessageServiceServicer):
    def GetResponse(self, request, context):
        input_message = request.message
        if detect(input_message) == "en":
            answer = extractor_en.domain_intent(prompt=input_message)
        elif detect(input_message) == "fa":
            answer = extractor_fa.domain_intent(prompt=input_message)
        else:
            answer = "Not a Supported Language!"
        response_message = f"{answer}"
        return MatchHub_pb2.MessageResponse(response=response_message)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    MatchHub_pb2_grpc.add_MessageServiceServicer_to_server(MessageService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
