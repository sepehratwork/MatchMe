import grpc
import MatchHub_pb2
import MatchHub_pb2_grpc
import time

def run():
    with grpc.insecure_channel('81.161.229.46:50051') as channel:
        s = time.time()
        stub_extractor = MatchHub_pb2_grpc.ExtractorgRPCStub(channel)
        response = stub_extractor.domain_intent(MatchHub_pb2.RequestDomainIntent(request="دوستم یه جفت جین میخواد"))
        e = time.time()
        print(f"Domain and Intent Extraction results: {response.response} in {e-s:.2f}")

        s = time.time()
        stub_captioner = MatchHub_pb2_grpc.ImageCaptioninggRPCStub(channel)
        response = stub_captioner.generate_caption(MatchHub_pb2.RequestCaption(request="sample.jpg"))
        e = time.time()
        print(f"Image Captioning results: {response.response} in {e-s:.2f}")

if __name__ == "__main__":
    run()
