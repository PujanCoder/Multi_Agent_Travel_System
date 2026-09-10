import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()


TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Create Tavily client
client = TavilyClient(api_key=TAVILY_API_KEY)


def tavily_search(query):
    response = client.search(
        query=query,
        max_results=5
    )

    result = []

    for i, r in enumerate(response["results"], 1):
        title = r.get("title", "Unknown")
        url = r.get("url", "")
        snippet = r.get("content", "").strip()

        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."

        result.append(
            f"{i}. **{title}**\n{url}\n{snippet}"
        )

    return "\n\n".join(result)