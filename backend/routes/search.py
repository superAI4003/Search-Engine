from fastapi import APIRouter, Depends, HTTPException
from search_engines.bing_search import BingSearch
from search_engines.google_search import GoogleSearch
from search_engines.wikipedia_search import WikipediaSearch
from llm_integration.llm_processor import LLMProcessor
router = APIRouter()


@router.get("/search")
async def search(query: str):
    googleSearch = GoogleSearch()
    google_results = googleSearch.search(query)
    return {"google_results":  str(google_results)}
