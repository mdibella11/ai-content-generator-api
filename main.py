
import os
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from dotenv import load_dotenv
import openai

load_dotenv()

app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Example API keys for authentication
VALID_API_KEYS = ["example-key-123", "example-key-456"]


class ContentRequest(BaseModel):
    topic: str
    keywords: list[str] = []
    length: int


@app.get("/health")
async def health():
    return {"status": "API is running", "author": "Marco Di Bella"}


@app.post("/generate")
async def generate_content(request: ContentRequest, x_api_key: str = Header(None)):
    if x_api_key not in VALID_API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    prompt = f"Write a {request.length}-word article about {request.topic}."
    if request.keywords:
        prompt += f" Include the following keywords: {', '.join(request.keywords)}."
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=request.length,
        )
        content = response.choices[0].text.strip()
        return {"author": "Marco Di Bella", "topic": request.topic, "content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
