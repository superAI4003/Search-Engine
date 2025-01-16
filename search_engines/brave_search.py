from search_engines.base_search_engine import BaseSearchEngine
import requests

class BraveSearch(BaseSearchEngine):
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.search.brave.com/res/v1/web/search"

    def search(self, query):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        params = {"q": query, "result_filter": "web"}
        response = requests.get(self.url, headers=headers, params=params)
        return response.json()