from fastapi import APIRouter, Depends, HTTPException
from llm_integration.llm_processor import LLMProcessor
from pydantic import BaseModel

class ConversationRequest(BaseModel):
    model_id: str
    prompt: str
router = APIRouter()

llm_processor = LLMProcessor()

@router.get("/models")
async def get_model_data():
    models_json = await llm_processor.models()  # Use await to call the async method
    return models_json

@router.post("/conversation")
async def conversation(request: ConversationRequest):
    models_json = await llm_processor.chat_completions(request.model_id, request.prompt)
    return models_json

@router.get("/get_credits")
async def conversation():
    models_json = await llm_processor.get_credits() # Use await to call the async method
    return models_json, 
''