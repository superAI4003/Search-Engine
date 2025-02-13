

import requests
import json
response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer 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",
      },
  data=json.dumps({
    "model": "openai/gpt-4o", # Optional
    "messages": [
      {
        "role": "user",
        "content": "What is the meaning of life?"
      }
    ]
  })
)
print(response.text)  