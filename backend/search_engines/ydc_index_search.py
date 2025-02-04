from .base_search_engine import BaseSearchEngine
import requests

class YDCIndexSearch(BaseSearchEngine):
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.ydc-index.io/search"

    def search(self, query):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        params = {"query": query}
        response = requests.get(self.url, headers=headers, params=params)
        return response.json()