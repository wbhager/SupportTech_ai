from fastapi import APIRouter
from pydantic import BaseModel
from backend.logic.orchestrator import orchestrate
from backend.logic.responder import respond_to_user
from backend.tools.web_search import web_search
from backend.tools.file_reader import file_reader
import json

router = APIRouter()

class Message(BaseModel):
    message: str

@router.post("/chat")
async def chat_endpoint(message: Message):
    tool_name, tool_args = orchestrate(message.message)
    
    print(f"DEBUG: tool_name={tool_name}, tool_args={tool_args}")

    tool_result = None
    searching = False

    if tool_name == "web_search":
        searching = True
        query = json.loads(tool_args)["query"]
        tool_result = web_search(query)

    if tool_name == "file_reader":
        file_path = json.loads(tool_args)["file_path"]
        query = json.loads(tool_args)["query"]
        tool_result = file_reader(file_path, query)

    response = respond_to_user(message.message, tool_name=tool_name, tool_result=tool_result)
    return {"response": response, "searching": searching}