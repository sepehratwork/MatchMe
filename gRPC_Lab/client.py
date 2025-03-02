import grpc
import grpc_lab_pb2
import grpc_lab_pb2_grpc

def run_service_a():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = grpc_lab_pb2_grpc.ServiceAStub(channel)
        request = grpc_lab_pb2.RequestA(param="World")
        response = stub.MethodA(request)
        print("ServiceA response:", response.result)

def run_service_b():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = grpc_lab_pb2_grpc.ServiceBStub(channel)
        request = grpc_lab_pb2.RequestB(id=42)
        response = stub.MethodB(request)
        print("ServiceB response:", response.message)

if __name__ == '__main__':
    run_service_a()
    run_service_b()
