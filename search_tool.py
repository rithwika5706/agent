from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

def search_web(query: str):
    """
    Search the web.
    """
    return search.run(query)