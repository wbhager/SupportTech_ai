from backend.eval.evaluator import evaluate_response
from backend.db import save_evaluation


async def run_evaluation_and_log(
    conv_id: str,
    message_id: str,
    user_message: str,
    qwen_response: str,
    tool_used: str | None,
    rag_used: bool
) -> None: 
    """
    Evaluates a Qwen response and logs the result to the database.
    """
    evaluation_result = await evaluate_response(
        user_query=user_message,
        qwen_response=qwen_response,
        tool_used=tool_used,
        rag_used=rag_used
    )

    if evaluation_result is None:
        print(f"[logger] There is no evaluation to log for message_id {message_id}.")
        return None

    save_evaluation(
        conv_id = conv_id,
        message_id = message_id,
        score = evaluation_result["score"],
        feedback = evaluation_result["feedback"]
    )