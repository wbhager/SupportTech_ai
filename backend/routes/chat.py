from fastapi import APIRouter
from pydantic import BaseModel
from backend.logic.orchestrator import orchestrate
from backend.logic.responder import respond_to_user
from backend.tools.web_search import web_search
from backend.tools.file_reader import file_reader
from backend.tools.log_parser import parse_python_traceback
import json

router = APIRouter()

class Message(BaseModel):
    message: str
    conv_id: str

@router.post("/chat")
async def chat_endpoint(message: Message):
    tool_name, tool_args, relevant_chunks = orchestrate(message.message, message.conv_id)
    
    print(f"DEBUG: tool_name={tool_name}, tool_args={tool_args}")

    tool_result = None
    searching = False

    if tool_name == "web_search":
        searching = True
        query = json.loads(tool_args)["query"]
        tool_result = web_search(query)

    if tool_name == "file_reader":
        file_path = json.loads(tool_args)["file_path"]
        query = json.loads(tool_args).get("query", "")
        tool_result = file_reader(file_path, query)

    if tool_name == "parse_log":
        text = json.loads(tool_args)["text"]
        query = json.loads(tool_args).get("query", "")
        parsed = parse_python_traceback(text)
        tool_result = f"{parsed}\n\nUser context: {query}" if query else str(parsed)

    response = respond_to_user(message.message, message.conv_id, tool_name=tool_name, tool_result=tool_result, relevant_chunks=relevant_chunks)
    return {"response": response, "searching": searching}