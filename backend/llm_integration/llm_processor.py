import httpx
import os

class LLMProcessor:
    def process(self, search_results):
        # Process the search results with LLMs
        pass
    async def models(self):
        url = "https://openrouter.ai/api/v1/models"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        
    async def chat_completions(self):
        url = "https://openrouter.ai/api/v1/chat/completions"
        api_key = os.getenv("OPENROUTER_API_KEY")
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "google/gemini-2.0-flash-thinking-exp:free",
            "messages": [
            {"role": "user", "content": "Hello"}
            ],
            "provider": {
            "ignore": [
                "Azure"
            ]
            }
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()