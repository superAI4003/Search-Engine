from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LLMOutputBase(BaseModel):
    llm_id :str
    query :str
    search_result :str
    llm_id:str
    llm_out :str
    prompt:str
    vote :bool
    class Config:
        form_attributes = True