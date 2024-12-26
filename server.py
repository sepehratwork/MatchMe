from concurrent import futures
import grpc
import MatchHub_pb2
import MatchHub_pb2_grpc

from main import Extractor
extractor = Extractor()

class MessageService(MatchHub_pb2_grpc.MessageServiceServicer):
    def GetResponse(self, request, context):
        input_message = request.message
        # Simple response logic
        answer = extractor.domain_intent(prompt=input_message)
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
