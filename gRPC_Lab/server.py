from concurrent import futures
import grpc
import time

# Import the generated classes
import grpc_lab_pb2
import grpc_lab_pb2_grpc

# Implementation for ServiceA
class ServiceAServicer(grpc_lab_pb2_grpc.ServiceAServicer):
    def MethodA(self, request, context):
        # Implement your business logic for MethodA
        print(f"Received request in MethodA with param: {request.param}")
        response = grpc_lab_pb2.ResponseA(result=f"Hello, {request.param} from ServiceA!")
        return response

# Implementation for ServiceB
class ServiceBServicer(grpc_lab_pb2_grpc.ServiceBServicer):
    def MethodB(self, request, context):
        # Implement your business logic for MethodB
        print(f"Received request in MethodB with id: {request.id}")
        response = grpc_lab_pb2.ResponseB(message=f"ServiceB received id {request.id}")
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Add both service implementations to the server
    grpc_lab_pb2_grpc.add_ServiceAServicer_to_server(ServiceAServicer(), server)
    grpc_lab_pb2_grpc.add_ServiceBServicer_to_server(ServiceBServicer(), server)
    
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    
    try:
        while True:
            time.sleep(86400)  # Keep the server running (1 day)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
