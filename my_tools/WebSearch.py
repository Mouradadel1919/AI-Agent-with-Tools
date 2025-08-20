import requests
from langchain_core.tools import Tool

def web_search(query):
    res = requests.post(
        "https://api.tavily.com/search",
        headers={"Authorization": "Bearer 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"},
        json={"query": query}
    )
    return res.json()["results"][0]["content"]



WebSearchTool = Tool.from_function(
    func=web_search,
    name="WebSearchTool",
    description="Use this tool if context is missing. Input should be the question, "
            "and it will return relevant information from the web."
)