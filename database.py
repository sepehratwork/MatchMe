import json
from langchain_core.documents import Document
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS


def save_domains_intents_into_db(embeddings, db_path="domain_intent_en", json_path="domain.json"):
    domains_intents = json.load(open(json_path, "r"))

    index = faiss.IndexFlatL2(len(embeddings.embed_query("MatchHub")))

    vector_store = FAISS(
        embedding_function=embeddings,
        index=index,
        docstore=InMemoryDocstore(),
        index_to_docstore_id={},
    )

    for i, domain in enumerate(domains_intents.keys()):
        for intent in domains_intents[domain].keys():
            examples = domains_intents[domain][intent]
            if len(examples) > 1:
                print(f"Adding examples of domain {domain} {i}/{len(domains_intents)} and intent {intent} with {len(examples)} examples")
                for i, example in enumerate(examples):
                    document = Document(
                        page_content=example,
                        metadata = {
                            "domain": domain,
                            "intent": intent
                        }
                    )
                    vector_store.add_documents(documents=[document], ids=[f"{domain}_{intent}_{i}"])
    
    vector_store.save_local(db_path)


# TODO
def add_to_vector_db(json_path, db_path="domain_intent"):
    pass


def load_vector_db(embeddings, path="domain_intent_en"):
    vector_store = FAISS.load_local(
        path, embeddings, allow_dangerous_deserialization=True
    )
    return vector_store
