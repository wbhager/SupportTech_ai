import os
import json
from openai import OpenAI
from dotenv import load_dotenv

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
            "description": "Read the contents of a file. The file can be in PDF, TXT, MD, PY, or JSON format.",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "The path to the file to be read.",
                    },
                    "query": {
                        "type": "string",
                        "description": "What the user wnats to know or do with the file",
                    }
                },
                "required": ["file_path"]
            }
        }
    }
]

def orchestrate(user_input):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": user_input}],
        tools=tools,
        tool_choice="auto"
    )

    tool_choice = response.choices[0].message

    if tool_choice.tool_calls:
        tool_name = tool_choice.tool_calls[0].function.name
        tool_args = tool_choice.tool_calls[0].function.arguments
        return tool_name, tool_args
    else:
        return "No tool call", None

    

