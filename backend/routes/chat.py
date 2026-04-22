from fastapi import APIRouter

router = APIRouter()

@router.post("/chat")
async def chat_endpoint(user_input: str):
    