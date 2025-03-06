import time

from main import Extractor, ImageCaptioning

s = time.time()
extractor_fa = Extractor(model_name="heydariAI/persian-embeddings", v_db="domain_intent_fa")
image_captioning = ImageCaptioning(model="blip")
e = time.time()
print(f"Models loaded in {e-s:.2f} seconds")

s = time.time()
answer_extractor = extractor_fa.domain_intent(prompt="دوستم یه جفت جین میخواد")
e = time.time()
print(f"Domain and Intent Extraction results: {answer_extractor} in {e-s:.2f}")

s = time.time()
answer_captioner = image_captioning.generate_caption(image_path="sample.jpg")
e = time.time()
print(f"Image Captioning results: {answer_captioner} in {e-s:.2f}")
