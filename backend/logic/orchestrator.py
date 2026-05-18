import os
import json
from openai import OpenAI

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

tools = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web for current information, recent events, or facts that may have changed over time. Do NOT use for general knowledge, conceptual questions, or anything that doesn't require up to date information."
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

    if choice.tool_calls:
        tool_name = choice.tool_calls[0].name
        tool_args = choice.tool_calls[0].arguments
        return tool_name, tool_args
    else:
        return "No tool call", None

    

