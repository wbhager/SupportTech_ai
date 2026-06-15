import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from backend.tools.memory import add_to_history, get_trimmed_history
from backend.tools.rag import retrieve_relevant_chunks

load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

tools = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web for any information about current events, scores, weather, prices, or anything that may have changed. When in doubt, search.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query to look up on the web.",
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "file_reader",
            "description": "Read the contents of a file. Only use this tool when the user provides a full absolute file path starting with /Users/",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "The full absolute path to the file, must start with /Users/. Example: /Users/willhager/Documents/SupportTech_ai/frontend-react/src/App.tsx"
                    },
                    "query": {
                        "type": "string",
                        "description": "What the user wnats to know or do with the file",
                    }
                },
                "required": ["file_path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "parse_log",
            "description": "Parses raw stack traces, error logs, and terminal output into structured data. Use when the user pastes an error, traceback, or any messy terminal output.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "The raw stack trace, error message, or terminal output to parse."
                    },
                    "query": {
                        "type": "string",
                        "description": "Optional additional context or hypothesis from the user about what the error might be doing."
                    }
                },
                "required": ["text"]
            }
        }
    }
]

def orchestrate(user_input: str, conv_id: str):
    relevant_chunks = retrieve_relevant_chunks(user_input)

    add_to_history(conv_id, role = "user", content = user_input)
    history = get_trimmed_history(conv_id, max_messages = 3)
    clean_history = [{"role": msg["role"], "content": msg["content"]} for msg in history]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=clean_history,
        tools=tools,
        tool_choice="auto"
    )

    tool_choice = response.choices[0].message

    if tool_choice.tool_calls:
        tool_name = tool_choice.tool_calls[0].function.name
        tool_args = tool_choice.tool_calls[0].function.arguments
        return tool_name, tool_args, relevant_chunks
    else:
        return "No tool call", None, relevant_chunks

    

