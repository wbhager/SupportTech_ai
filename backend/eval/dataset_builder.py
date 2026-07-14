import json
from backend.db import cursor  # or whatever accessor your db.py exposes for raw queries

SCORE_THRESHOLD = 4  # TODO: does this match what you'd consider "good enough" on a 1-5 scale?
OUTPUT_PATH = "training_data.jsonl"


def get_high_scoring_message_ids(threshold: int) -> list[int]:
    """Returns message_ids from evaluations table with score >= threshold."""
    # TODO: SELECT message_id FROM evaluations WHERE score >= %s
    ...


def get_training_pair(message_id: int) -> dict | None:
    """
    Given an assistant message_id, finds the user question that preceded it
    and returns {"instruction": ..., "response": ...}, or None if no
    matching user message is found.
    """
    # TODO 1: fetch this message's conv_id, message_order, and content
    #         (SELECT conv_id, message_order, content FROM messages WHERE message_id = %s)

    # TODO 2: using that conv_id and message_order, find the user message
    #         at message_order - 1
    #         (SELECT content FROM messages WHERE conv_id = %s AND message_order = %s AND role = 'user')

    # TODO 3: return {"instruction": user_content, "response": assistant_content}
    #         or None if step 2 found nothing
    ...


def build_dataset():
    message_ids = get_high_scoring_message_ids(SCORE_THRESHOLD)
    print(f"Found {len(message_ids)} high-scoring messages")

    pairs = []
    for msg_id in message_ids:
        pair = get_training_pair(msg_id)
        if pair:
            pairs.append(pair)

    # TODO: write `pairs` to OUTPUT_PATH as JSONL (one JSON object per line)

    print(f"Wrote {len(pairs)} training pairs to {OUTPUT_PATH}")


if __name__ == "__main__":
    build_dataset()