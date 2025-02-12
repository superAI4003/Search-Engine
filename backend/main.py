from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from search_engines.bing_search import BingSearch
from search_engines.google_search import GoogleSearch
from search_engines.wikipedia_search import WikipediaSearch
from llm_integration.llm_processor import LLMProcessor
from dotenv import load_dotenv
import os
from routes import search, llm,llm_output

 
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
 
load_dotenv()
 
app.include_router(search.router, prefix="/search", tags=["Search"])   
app.include_router(llm.router, prefix="/llm", tags=["LLM"]) 
app.include_router(llm_output.router, prefix="/api", tags=["LLMOutput"])
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)