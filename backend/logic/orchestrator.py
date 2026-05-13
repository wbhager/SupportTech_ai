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

