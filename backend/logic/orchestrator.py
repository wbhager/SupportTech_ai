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

    

