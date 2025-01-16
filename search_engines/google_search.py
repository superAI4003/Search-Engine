from .base_search_engine import BaseSearchEngine
import requests

class GoogleSearch(BaseSearchEngine):
    def __init__(self, api_key, cx):
        self.api_key = api_key
        self.cx = cx
        self.url = "https://www.googleapis.com/customsearch/v1"

    def search(self, query):
        params = {"q": query, "key": self.api_key, "cx": self.cx}
        response = requests.get(self.url, params=params)
        return response.json()