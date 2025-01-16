from search_engines.bing_search import BingSearch
from search_engines.google_search import GoogleSearch
from search_engines.wikipedia_search import WikipediaSearch
from llm_integration.llm_processor import LLMProcessor
from dotenv import load_dotenv
import os

def main():
    # Load environment variables from .env file
    load_dotenv()

    query = "example search"
    
    # Initialize search engines with API keys from environment variables
    bing = BingSearch(api_key=os.getenv("BING_API_KEY"))
    google = GoogleSearch(api_key=os.getenv("GOOGLE_API_KEY"), cx=os.getenv("GOOGLE_CX"))
    wikipedia = WikipediaSearch()
    
    # Perform searches
    bing_results = bing.search(query)
    google_results = google.search(query)
    wikipedia_results = wikipedia.search(query)
    
    # Process results with LLMs
    llm_processor = LLMProcessor()
    llm_processor.process(bing_results)
    llm_processor.process(google_results)
    llm_processor.process(wikipedia_results)

if __name__ == "__main__":
    main()