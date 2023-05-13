
import time
from duckduckgo_search import ddg
import json

from . import config
def main(obj):
    while True:
        try:
            o=main1(obj)
            return json.dumps(o)
        except:
            time.sleep(3)
def main1(obj):
    query,num_results=obj['query'],obj['num_results']
    search_results = []
    if not query:
        return json.dumps(search_results)

    results = ddg(query, max_results=num_results)
    if not results:
        return json.dumps(search_results)

    for j in results:
        search_results.append(j)

    results = json.dumps(search_results, ensure_ascii=False, indent=4)
    return safe_google_results(results)


def safe_google_results(results: str | list) -> str:
    """
        Return the results of a google search in a safe format.

    Args:
        results (str | list): The search results.

    Returns:
        str: The results of the search.
    """
    if isinstance(results, list):
        safe_message = json.dumps(
            [result.encode("utf-8", "ignore") for result in results]
        )
    else:
        safe_message = results.encode("utf-8", "ignore").decode("utf-8")
    return safe_message
