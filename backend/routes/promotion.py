from fastapi import APIRouter, HTTPException
from backend.db import conn, cursor  # adjust to your actual db module
from backend.utility_funcs import promote, reject  # adjust to your actual file

router = APIRouter(prefix="/api", tags=["promotion"])


@router.get("/candidates")
def get_candidates(limit: int = 20):
    cursor.execute(
        """
        SELECT evaluation_id, score, feedback, user_message, qwen_response
        FROM evaluations
        WHERE score = 5 AND promotion_status = 'pending'
        ORDER BY evaluation_id DESC
        LIMIT %s
        """,
        (limit,),
    )
    rows = cursor.fetchall()
    cols = [desc[0] for desc in cursor.description]
    return [dict(zip(cols, row)) for row in rows]


@router.post("/candidates/{evaluation_id}/promote")
def promote_candidate(evaluation_id: int):
    try:
        promote(conn, evaluation_id, prompt_path="backend/prompts/system_prompt.txt")
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"status": "approved", "evaluation_id": evaluation_id}


@router.post("/candidates/{evaluation_id}/reject")
def reject_candidate(evaluation_id: int):
    reject(conn, evaluation_id)
    return {"status": "rejected", "evaluation_id": evaluation_id}


@router.get("/example-history")
def get_example_history():
    cursor.execute(
        "SELECT id, source_evaluation_id, example_content, promoted_at "
        "FROM example_history ORDER BY id DESC"
    )
    rows = cursor.fetchall()
    cols = [desc[0] for desc in cursor.description]
    return [dict(zip(cols, row)) for row in rows]