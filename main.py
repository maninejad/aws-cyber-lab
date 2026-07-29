from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
import os

app = FastAPI()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def call_llm(message: str) -> str:
    """Wrapper so the model/provider can be swapped later without touching the rest of the app."""
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=message
    )
    return response.text

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    reply = call_llm(request.message)
    return {"reply": reply}
