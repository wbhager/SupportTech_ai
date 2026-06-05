from collections import defaultdict
import uuid

conv_history = defaultdict(list)

def add_to_history(conv_id: str = str(uuid.uuid4()), role: str, content: str) -> None:
    """Add a single message to a conversation's history."""
    conv_history[conv_id].append({"role": role, "content": content, "msg_id": str(uuid.uuid4())})

def get_history(conv_id: str) -> list:
    """Return the full message history for a given conversation."""
    pass

def get_trimmed_history(conv_id: str, max_messages: int = 20) -> list:
    """Return only the last max_messages messages for a given conversation."""
    pass

def delete_history(conv_id: str = None) -> None:
    """Delete history for a specific conversation, or all conversations if no conv_id given."""
    pass