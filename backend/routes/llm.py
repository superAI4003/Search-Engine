from fastapi import APIRouter, Depends, HTTPException
from llm_integration.llm_processor import LLMProcessor
router = APIRouter()

llm_processor = LLMProcessor()

@router.get("/models")
async def get_model_data():
    models_json = await llm_processor.models()  # Use await to call the async method
    return models_json

@router.get("/conversation")
async def conversation():
    models_json = await llm_processor.chat_completions()  # Use await to call the async method
    return models_json