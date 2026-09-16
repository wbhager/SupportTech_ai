import re

# Example formatting function
def format_as_example(user_message: str, qwen_response: str) -> str:
    return f"Q: {user_message}\nA: {qwen_response}"

# Writing in the new example which replaces old example function
START_MARKER = "<!-- ROTATING_EXAMPLE_START -->"
END_MARKER = "<!-- ROTATING_EXAMPLE_END -->"

def write_rotating_example(new_example_text: str, prompt_path: str) -> None:
    with open(prompt_path, "r", encoding="utf-8") as f:
        original = f.read()

    pattern = re.compile(re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL)

    if not pattern.search(original):
        raise ValueError("Markers not found — aborting write.")

    new_block = f"{START_MARKER}\n{new_example_text}\n{END_MARKER}"
    updated = pattern.sub(new_block, original, count=1)

    # confirm nothing outside the markers changed
    if pattern.sub("", original) != pattern.sub("", updated):
        raise RuntimeError("Content outside markers changed — file NOT written.")

    with open(prompt_path, "w", encoding="utf-8") as f:
        f.write(updated)

# Promote five star response from pending to approved
def promote(conn, evaluation_id: int, prompt_path: str) -> None:
    with conn.cursor() as cur:
        cur.execute(
            "SELECT evaluation_id, user_message, qwen_response FROM evaluations "
            "WHERE evaluation_id = %s AND promotion_status = 'pending'",
            (evaluation_id,),
        )
        row = cur.fetchone()

    if row is None:
        raise ValueError(f"Evaluation {evaluation_id} not found or not pending.")

    eval_id, user_message, qwen_response = row
    formatted = format_as_example(user_message, qwen_response)

    write_rotating_example(formatted, prompt_path)  # file write first, DB after

    with conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO example_history (source_evaluation_id, example_content) VALUES (%s, %s)",
                (eval_id, formatted),
            )
            cur.execute(
                "UPDATE evaluations SET promotion_status = 'approved' WHERE evaluation_id = %s",
                (eval_id,),
            )