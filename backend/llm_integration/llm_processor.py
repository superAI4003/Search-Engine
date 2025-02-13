import httpx
import os
import json

class LLMProcessor:
    def process(self, search_results):
        # Process the search results with LLMs
        pass
    def get_context_length(self, model_id, json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        for model in data['data']:
            if model['id'] == model_id:
                return model['context_length']
    
        return None  # Return None if the model_id is not found

    async def chat_completions(self, model_id="google/gemini-2.0-flash-thinking-exp:free", prompt="Hi"):
        json_file_path = 'llm_integration/modelinfo.json'
        context_length = self.get_context_length(model_id, json_file_path)
        if len(prompt) > context_length:
            prompt = prompt[:context_length]
        url = "https://openrouter.ai/api/v1/chat/completions"
        api_key = os.getenv("OPENROUTER_API_KEY")
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": model_id,  # Use the model_id parameter
            "messages": [
                {"role": "user", "content": prompt}  # Use the prompt parameter
            ],
        }


        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json() 
    async def models(self):
        url = "https://openrouter.ai/api/v1/models"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        
        
    async def get_credits(self):
        url = "https://openrouter.ai/api/v1/credits"
        api_key = os.getenv("OPENROUTER_API_KEY")
        headers = {
            "Authorization": f"Bearer {api_key}"
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
    