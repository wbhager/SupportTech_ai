import chromadb
from sentence_transformers import SentenceTransformer
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent 
EMBEDDINGS_PATH = str(BASE_DIR / "data" / "embeddings")

embedding_model = SentenceTransformer("all-mpnet-base-v2")
chroma_client = chromadb.PersistentClient(path=EMBEDDINGS_PATH)
collection = chroma_client.get_or_create_collection("supporttech_docs")

def retrieve_relevant_chunks(query: str, top_k: int = 3) -> list[str]:
    embedding = embedding_model.encode(query).tolist()
    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )
    return results["documents"][0]