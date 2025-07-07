from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
def chat(req: ChatRequest):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": req.prompt, "stream": False}
    )
    return {"response": response.json().get("response", "No response")}

