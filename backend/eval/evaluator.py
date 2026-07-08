import anthropic
from dotenv import load_dotenv
import json
import os
from pathlib import Path

load_dotenv()

client = Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))
EVALUATOR_PROMPT = Path("backend/prompt/eval_prompt.txt").read_text()

async def evaluate_response(
    user_query: str,
    qwen_response: str,
    tool_used: str | None,
    rag_used: bool,
) -> dict:
    """
    Calls Claude Sonnet to score a Qwen response 1-5 with brief feedback.
    Pure function: no DB access, no side effects. Caller is responsible
    for persisting the result.

    Returns: {"score": int, "feedback": str}
    Raises: on malformed Claude output (caller decides retry/skip policy)
    """

    user_content = 
    f"""
    User's question: {user_query}
    Tool used: {tool_used if tool_used else "None"}
    RAG used: {"Yes" if rag_used else "No"}
    Response to evaluate: {qwen_response}
    """

    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        system=EVALUATOR_PROMPT,
        max_tokens=500,
        messages=[
            {"role": "user", "content": user_content}
        ],
    )

    # TODO 3: extract the text from the response
    # (response.content is a list of blocks — you want the text block)
    raw_output = ...

    # TODO 4: parse + validate (you already sketched this earlier —
    # json.loads, check score is int 1-5, check "feedback" key exists)
    result = parse_evaluation(raw_output)

    return result


def parse_evaluation(claude_output: str) -> dict:
    try:
        result = json.loads(claude_output)
        score = int(result["score"])
        if not 1 <= score <= 5:
            raise ValueError(f"score out of range: {score}")
        return {"score": score, "feedback": result["feedback"]}
    except (json.JSONDecodeError, KeyError, ValueError) as e:
        # TODO 5: decide policy here — re-raise for caller to handle,
        # log and return a sentinel value, or retry once inline?
        raise