import chromadb
from sentence_transformers import SentenceTransformer
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent 
EMBEDDINGS_PATH = str(BASE_DIR / "data" / "embeddings")

embedding_model = SentenceTransformer("BAAI/bge-large-en-v1.5")
chroma_client = chromadb.PersistentClient(path=EMBEDDINGS_PATH)
collection = chroma_client.get_or_create_collection("supporttech_docs")

def retrieve_relevant_chunks(query: str, top_k: int = 5) -> list[str]:
    embedding = embedding_model.encode(query).tolist()
    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k,
        include=["documents", "distances"]
    )
    
    chunks = []
    for doc, distance in zip(results["documents"][0], results["distances"][0]):
        print(f"DEBUG RAG distance: {distance:.4f} | chunk preview: {doc[:80]}...")
        if distance < 0.6:
            chunks.append(doc)
    
    print(f"DEBUG RAG: {len(chunks)} chunks passed threshold")
    return chunks