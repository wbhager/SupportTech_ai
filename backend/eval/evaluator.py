from anthropic import Anthropic
from dotenv import load_dotenv
import json
import os
from pathlib import Path

load_dotenv()

client = Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))
EVALUATOR_PROMPT = Path("backend/prompts/eval_prompt.txt").read_text()
QWEN_SYSTEM_PROMPT = Path("backend/prompts/system_prompt.txt").read_text()

async def evaluate_response(
    user_message: str,
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
    try:
        user_content = f"""The assistant being evaluated follows these instructions:
            {QWEN_SYSTEM_PROMPT}

            User's question: {user_message}
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

        raw_output = response.content[0].text.strip()
        result = parse_evaluation(raw_output)
        return result

    except Exception as e:
        print(f"Error during evaluation: {e}")
        return None


def parse_evaluation(claude_output: str) -> dict:
    try:
        cleaned = claude_output.strip()
        if cleaned.startswith("```"):
            cleaned = cleaned.split("\n", 1)[1]
            cleaned = cleaned.rsplit("```", 1)[0]
            cleaned = cleaned.strip()

        result = json.loads(cleaned)
        score = int(result["score"])
        if not 1 <= score <= 5:
            raise ValueError(f"score out of range: {score}")
        return {"score": score, "feedback": result["feedback"]}
    except (json.JSONDecodeError, KeyError, ValueError) as e:
        print(f"Error parsing evaluation output: {e}. Output was: {claude_output}")
        return None