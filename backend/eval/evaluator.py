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

    # TODO 1: build the user-turn content.
    # Needs to clearly present: the question, Qwen's response, and the
    # tool_used/rag_used context (label it clearly so Claude doesn't confuse
    # it with the response itself — e.g. a short "Context:" section vs the
    # actual "Response to evaluate:" section)
    user_content = ...

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