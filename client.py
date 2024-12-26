import grpc
import MatchHub_pb2
import MatchHub_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = MatchHub_pb2_grpc.MessageServiceStub(channel)
        response = stub.GetResponse(MatchHub_pb2.MessageRequest(message="I need some T-shirts!"))
        print(f"Server response: {response.response}")

if __name__ == "__main__":
    run()
