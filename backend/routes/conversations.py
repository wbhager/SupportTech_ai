from fastapi import APIRouter
from backend.db import fetch_sidebar_conv_names, get_conversation_history

router = APIRouter()

@router.get("/conversations")
async def get_sidebar_title_names():
    conv_names = fetch_sidebar_conv_names()
    return {"conversations": [{"conv_id": conv_id, "title": title} for conv_id, title in conv_names]}

@router.get("/conversations/{conv_id}/messages")
async def get_conversation_messages(conv_id: str):
    conv_messages = get_conversation_history(conv_id)
    return {"messages": [{"role": role, "content": content} for role, content in conv_messages]}

