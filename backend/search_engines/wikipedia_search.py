from .base_search_engine import BaseSearchEngine
import requests

class WikipediaSearch(BaseSearchEngine):
    def __init__(self):
        self.url = "https://en.wikipedia.org/w/api.php"

    def search(self, query):
        params = {
            "action": "opensearch",
            "search": query,
            "limit": "10",
            "namespace": "0",
            "format": "json"
        }
        response = requests.get(self.url, params=params)
        return response.json()