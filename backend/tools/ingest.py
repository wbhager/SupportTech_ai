import chromadb
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
chroma_client = chromadb.PersistentClient(path="backend/data/embeddings")
collection = chroma_client.get_or_create_collection("supporttech_docs")

files = [
    "frontend-react/src/App.tsx",
    "backend/logic/orchestrator.py",
    "backend/logic/responder.py"
]

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> list[str]:
    
