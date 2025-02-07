import grpc
import MatchHub_pb2
import MatchHub_pb2_grpc
import time

def run():
    s = time.time()
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = MatchHub_pb2_grpc.MessageServiceStub(channel)
        response = stub.GetResponse(MatchHub_pb2.MessageRequest(message="دوستم یه جفت جین میخواد"))
        e = time.time()
        print(f"Server response: {response.response} in {e-s:.2f}")

if __name__ == "__main__":
    run()
