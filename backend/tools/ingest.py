import chromadb
from sentence_transformers import SentenceTransformer
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent 
EMBEDDINGS_PATH = str(BASE_DIR / "data" / "embeddings")

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
chroma_client = chromadb.PersistentClient(path=EMBEDDINGS_PATH)
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
    print(f"Ingesting: {filepath}")
    text = Path(filepath).read_text()
    filename = Path(filepath).name
    print(f"Text length: {len(text)}")
    chunks = chunk_text(text)
    print(f"Chunks created: {len(chunks)}")

    for i, chunk in enumerate(chunks):
        contextualized_chunk = f"File: {filename}\n\n{chunk}"
        chunk_id = filename + f"_{i}"
        embedding = embedding_model.encode(contextualized_chunk).tolist()
        collection.upsert(
            ids=[chunk_id],
            embeddings=[embedding],
            documents=[contextualized_chunk],
            metadatas=[{"source": filepath}]
        )
    print(f"Done ingesting {filepath}")

def ingest_all() -> None:
    for filepath in files:
        ingest_file(filepath)
    print(f"Total chunks in collection: {collection.count()}")

if __name__ == "__main__":
    ingest_all()
