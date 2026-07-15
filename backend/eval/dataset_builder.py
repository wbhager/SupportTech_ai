import json
from backend.db import cursor

SCORE_THRESHOLD = 4 
OUTPUT_PATH = "backend/data/training/training_data.jsonl"

def build_dataset():
    """
    Pulls all high-scoring evaluations and writes them out as a JSONL
    training file in {"instruction": ..., "response": ...} format.
    """
    cursor.execute(
        "SELECT user_message, qwen_response FROM evaluations WHERE score >= %s",
        (SCORE_THRESHOLD,)
    )
    rows = cursor.fetchall()

    pairs = [{"instruction": q, "response": r} for q, r in rows]

    with open(OUTPUT_PATH, "w") as f:
        for pair in pairs:
            f.write(json.dumps(pair) + "\n")

    print(f"Wrote {len(pairs)} training pairs to {OUTPUT_PATH}")

if __name__ == "__main__":
    build_dataset()