import json
from uuid import uuid4
from tqdm import tqdm
from langchain_core.documents import Document
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS

from main import embeddings


def save_domains_intents():
    domains_intents = json.load(open("domain.json", "r"))

    index = faiss.IndexFlatL2(len(embeddings.embed_query("MatchHub")))

    vector_store = FAISS(
        embedding_function=embeddings,
        index=index,
        docstore=InMemoryDocstore(),
        index_to_docstore_id={},
    )

    for domain in domains_intents.keys():
        for intent in domains_intents[domain].keys():
            examples = domains_intents[domain][intent]
            for i, example in tqdm(enumerate(examples), desc=f"Adding examples of domain {domain} and intent {intent}"):
                document = Document(
                    page_content=example,
                    metadata = {
                        "domain": domain,
                        "intent": intent
                    }
                )
                vector_store.add_documents(documents=[document], ids=[f"{domain}_{intent}_{i}"])
    
    vector_store.save_local("domain_intent")


def load_domains_intents():
    vector_store = FAISS.load_local(
        "faiss_index", embeddings, allow_dangerous_deserialization=True
    )
    return vector_store
