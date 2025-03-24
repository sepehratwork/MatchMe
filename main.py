import base64
from PIL import Image
import torch
from groq import Groq
# from transformers import Blip2Processor, Blip2ForConditionalGeneration, GitProcessor, GitForCausalLM
from langchain_huggingface import HuggingFaceEmbeddings
from deep_translator import GoogleTranslator

import config
from database import load_vector_db


class Extractor:
    def __init__(self, model_name="sentence-transformers/all-mpnet-base-v2", v_db="domain_intent_en"):
        self.v_db = v_db
        model_kwargs = {'device': 'cpu'}
        encode_kwargs = {'normalize_embeddings': False}
        self.embeddings = HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs
        )

        try:
            self.vector_store = load_vector_db(self.embeddings, path=v_db)
        except:
            pass
            # raise EnvironmentError("The given path has not been set for the vector database")

    def domain_intent(self, prompt, k=1, filter=None, threshold=0.2):
        results = self.vector_store.similarity_search_with_relevance_scores(
            query=prompt,
            k=k,
            filter=filter
        )
        for res, score in results:
            if score > threshold:
                return res.metadata


class ImageCaptioning:
    def __init__(self, model="blip", local=False):
        if not local:
            self.client = Groq(api_key=config.groq_api_key)
        # else:
        #     self.device = "cuda" if torch.cuda.is_available() else "cpu"
        #     if model == "blip":
        #         self.processor = Blip2Processor.from_pretrained(
        #             "Salesforce/blip2-flan-t5-xl"
        #             # "Salesforce/blip2-opt-2.7b"
        #             )
        #         self.model = Blip2ForConditionalGeneration.from_pretrained(
        #             "Salesforce/blip2-flan-t5-xl",
        #             # "Salesforce/blip2-opt-2.7b",
        #             torch_dtype=torch.float16
        #         )
        #         self.model.to(self.device)
        #     elif model == "git":
        #         self.processor = GitProcessor.from_pretrained("microsoft/git-base-coco")
        #         self.model = GitForCausalLM.from_pretrained("microsoft/git-base-coco")
        #         self.model.to(self.device)

    def generate_caption(self, image_path):
        # Inputs
        image = Image.open(image_path)
        text_prompt = \
        """Request: Provide a thorough description of the image. Include as many as aspects and details as you can, e.g., color, brand, material, gender and etc.
        Answer:"""

        # Process inputs
        inputs = self.processor(
            text=text_prompt,
            images=image,
            return_tensors="pt",
            padding=True
        ).to(self.device, torch.float16)

        # Generate
        generated_ids = self.model.generate(
            **inputs,
            # pixel_values=inputs.pixel_values,
            # input_ids=inputs.input_ids,
            # attention_mask=inputs.attention_mask,
            # early_stopping=True,
            max_new_tokens=1000,
            num_beams=5
        )

        # Decode
        result = self.processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        answer = result.split("Answer:")[-1].strip()
        answer = GoogleTranslator(source='en', target='fa').translate(answer)
        return answer
    
    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    
    def generate_caption_groq(self, image_path):
        # Getting the base64 string
        base64_image = self.encode_image(image_path)

        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What's in this image?"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}",
                            },
                        },
                    ],
                }
            ],
            model="llama-3.2-11b-vision-preview",
        )

        return chat_completion.choices[0].message.content

