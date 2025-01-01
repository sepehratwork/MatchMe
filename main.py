from langchain_huggingface import HuggingFaceEmbeddings

from database import load_vector_db

class Extractor:
    def __init__(self, model_name="sentence-transformers/all-mpnet-base-v2"):
        model_kwargs = {'device': 'cpu'}
        encode_kwargs = {'normalize_embeddings': False}
        self.embeddings = HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs
        )

        try:
            self.vector_store = load_vector_db(self.embeddings)
        except:
            raise EnvironmentError("The given path has not been set for the vector database")
    
    def domain_intent(self, prompt, k=1, filter=None, threshold=0.2):
        results = self.vector_store.similarity_search_with_relevance_scores(
            query=prompt,
            k=k,
            filter=filter
        )
        for res, score in results:
            if score > threshold:
                return res.metadata
    
