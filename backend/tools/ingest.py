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
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def ingest_file(filepath: str) -> None:
    text = Path(filepath).read_text()
    chunks = chunk_text(text)

    for i, chunk in enumerate(chunks):
        chunk_id = Path(filepath).name+ f"_{i}"
        embedding = embedding_model.encode(chunk).tolist()
        collection.add(
            ids=[chunk_id],
            embeddings=[embedding],
            documents=[chunk],
            metadatas=[{"source": filepath}]
        )

def ingest_all() -> None:
    for filepath in files:
        ingest_file(filepath)
