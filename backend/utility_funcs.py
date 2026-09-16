# Example formatting function
def format_as_example(user_message: str, qwen_response: str) -> str:
    return f"Q: {user_message}\nA: {qwen_response}"