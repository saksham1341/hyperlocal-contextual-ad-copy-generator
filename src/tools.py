"""
LLM Tools
"""

from config import SERPER_API_KEY, SERPER_TBS
import json
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.tools import tool

@tool(
    name_or_callable="search_internet",
)
def search_internet(context_type: str, query: str, gl: str, location: str) -> dict:
    """
    Search the internet and get real-time results for any query at given location.
    
    Args:
        context_type (str): The context type being searched for. Used when compiling raw context search results.
        query (str): The query to search.
        gl (str): The country to filter the search.
        location (str): Specific location to filter the search.
    """
    
    _ = GoogleSerperAPIWrapper(
        gl=gl,
        type="search",
        tbs=SERPER_TBS,
        serper_api_key=SERPER_API_KEY
    )
    
    results = _.results(
        query=query,
        location=location
    )
    
    return json.dumps({
        "context_type": context_type,
        "results": results
    })

# if __name__ == "__main__":
#     print(search_internet.description)
#     # print(search_internet({"query": "What are the latest Social Media Trends in Noida, Uttar Pradesh?", "gl": "in", "location": "Noida, Uttar Pradesh, India"}))
