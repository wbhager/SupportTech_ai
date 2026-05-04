from fastapi import APIRouter
from pydantic import BaseModel
from backend.logic.generate_response import generate_response

router = APIRouter()

class Message(BaseModel):
    message: str

@router.post("/chat")
async def chat_endpoint(message: Message):
    response = generate_response(message.message)
    return {"response": response}