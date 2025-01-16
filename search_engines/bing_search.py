from .base_search_engine import BaseSearchEngine
import requests

class BingSearch(BaseSearchEngine):
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.bing.microsoft.com/v7.0/search"

    def search(self, query):
        headers = {"Ocp-Apim-Subscription-Key": self.api_key}
        params = {"q": query}
        response = requests.get(self.url, headers=headers, params=params)
        return response.json()