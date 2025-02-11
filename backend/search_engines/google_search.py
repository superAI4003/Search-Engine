from .base_search_engine import BaseSearchEngine
from dotenv import load_dotenv
import os
import requests

class GoogleSearch(BaseSearchEngine):
    def __init__(self ):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.cx = os.getenv("GOOGLE_CX")
        self.url = "https://www.googleapis.com/customsearch/v1"

    def search(self, query):
        params = {"q": query, "key": self.api_key, "cx": self.cx}
        response = requests.get(self.url, params=params)
        return response.json()