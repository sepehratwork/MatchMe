import time
from langdetect import detect
from concurrent import futures
import grpc
import MatchHub_pb2
import MatchHub_pb2_grpc

from main import Extractor, ImageCaptioning

s = time.time()
# extractor_en = Extractor(model_name="sentence-transformers/all-mpnet-base-v2", v_db="domain_intent_en")
extractor_fa = Extractor(model_name="heydariAI/persian-embeddings", v_db="domain_intent_fa")
image_captioning = ImageCaptioning(model="blip", local=False)
e = time.time()
print(f"Models loaded in {e-s:.2f} seconds")


class ExtractorgRPC(MatchHub_pb2_grpc.ExtractorgRPCServicer):
    def domain_intent(self, request, context):
        input_message = request.request
        if detect(input_message) == "fa":
            answer = extractor_fa.domain_intent(prompt=input_message)
        # elif detect(input_message) == "en":
        #     answer = extractor_en.domain_intent(prompt=input_message)
        else:
            answer = "Not a Supported Language!"
        response_message = f"{answer}"
        return MatchHub_pb2.ResponseDomainIntent(response=response_message)


class ImageCaptioninggRPC(MatchHub_pb2_grpc.ImageCaptioninggRPCServicer):
    def generate_caption(self, request, context):
        input_message = request.request
        answer = image_captioning.generate_caption_groq(url=input_message)
        response_message = f"{answer}"
        return MatchHub_pb2.ResponseCaption(response=response_message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    MatchHub_pb2_grpc.add_ExtractorgRPCServicer_to_server(ExtractorgRPC(), server)
    MatchHub_pb2_grpc.add_ImageCaptioninggRPCServicer_to_server(ImageCaptioninggRPC(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
