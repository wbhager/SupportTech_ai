# backend/eval/evaluator.py

import anthropic
import json
import os

# TODO: load the evaluator system prompt from backend/prompts/evaluator_prompt.txt
# (reuse whatever pattern orchestrator.py / responder.py already use for this)


client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

orchestrator_prompt = Path(__file__).parent.parent / "prompts" / "orchestrator_prompt.txt"
orchestrator_prompt = orchestrator_prompt.read_text()



EVALUATOR_PROMPT = ...

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


async def evaluate_response(
    user_question: str,
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

    # TODO 2: make the API call
    # - model: which Claude model string? (check product-self-knowledge 
    #   for current valid model strings)
    # - system: EVALUATOR_PROMPT
    # - messages: [{"role": "user", "content": user_content}]
    # - max_tokens: this response is tiny (JSON + a sentence) — keep it small
    response = client.messages.create(
        model=...,
        system=EVALUATOR_PROMPT,
        max_tokens=...,
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