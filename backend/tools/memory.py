from collections import defaultdict
import uuid
from backend.db import save_conversation, save_message, get_conversation_history, delete_conversation

conv_history = defaultdict(list)

def add_to_history(conv_id: str, role: str, content: str) -> None:
    """Add a single message to a conversation's history."""
    conv_history[conv_id].append({"role": role, "content": content})
    save_conversation(conv_id)
    save_message(conv_id, role, content)

def get_history(conv_id: str) -> list:
    """Return the full message history for a given conversation."""
    if conv_id not in conv_history:
        db_history = get_conversation_history(conv_id)
        if db_history:
            for role, content in db_history:
                conv_history[conv_id].append({"role": role, "content": content})
    return conv_history[conv_id]

def get_trimmed_history(conv_id: str, max_messages: int = 4) -> list:
    """Return only the last max_messages messages for a given conversation."""
    return get_history(conv_id)[-max_messages:]

def delete_history(conv_id: str = None) -> None:
    """Delete history for a specific conversation"""
    del conv_history[conv_id]
    delete_conversation(conv_id)

