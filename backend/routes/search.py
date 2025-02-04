from fastapi import APIRouter, Depends, HTTPException
from search_engines.bing_search import BingSearch
from search_engines.google_search import GoogleSearch
from search_engines.wikipedia_search import WikipediaSearch
from llm_integration.llm_processor import LLMProcessor
router = APIRouter()


@router.get("/search")
async def search(query: str):
    # Perform searches
    # bing_results = bing.search(query)
    # google_results = google.search(query)
    wikipedia = WikipediaSearch()
    wikipedia_results = wikipedia.search(query)
    
    # Process results with LLMs
    # llm_processor = LLMProcessor()
    # llm_processor.process(bing_results)
    # llm_processor.process(google_results)
    # llm_processor.process(wikipedia_results)
    
    return {"wikipedia_results": wikipedia_results}
