from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from search_engines.bing_search import BingSearch
from search_engines.google_search import GoogleSearch
from search_engines.wikipedia_search import WikipediaSearch
from llm_integration.llm_processor import LLMProcessor
from dotenv import load_dotenv
import os
from routes import search, llm

# Initialize FastAPI app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
# Load environment variables from .env file
load_dotenv()

# Initialize search engines with API keys from environment variables
# bing = BingSearch(api_key=os.getenv("BING_API_KEY"))
# google = GoogleSearch(api_key=os.getenv("GOOGLE_API_KEY"), cx=os.getenv("GOOGLE_CX"))
app.include_router(search.router, prefix="/search", tags=["Search"])  #prompt handling
app.include_router(llm.router, prefix="/llm", tags=["LLM"]) 

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)