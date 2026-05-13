from tavily import TavilyClient
import os

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def web_search(query):
    response = client.search(query)
    results = response["results"]
    formatted = "\n\n".join([r["content"] for r in results])
    return formatted
