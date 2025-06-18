
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatRequest(BaseModel):
    message: str
    chat_history: list = []

@app.post("/chat")
async def chat_endpoint(chat_request: ChatRequest):
    if not chat_request.chat_history:
        chat_request.chat_history.append({
            "role": "system",
            "content": (
                "Sa oled tööintervjuu läbiviija, kes küsib tööintervjuu küsimusi eesti keeles. "
                "Kui kandidaat vastab, siis hinda iga vastust skaalal 1 kuni 10 ja põhjenda hinnet."
            )
        })

    chat_request.chat_history.append({"role": "user", "content": chat_request.message})

    response = client.chat.completions.create(
        model="gpt-4",
        messages=chat_request.chat_history
    )

    assistant_msg = response.choices[0].message.content
    chat_request.chat_history.append({"role": "assistant", "content": assistant_msg})

    return {"reply": assistant_msg, "chat_history": chat_request.chat_history}
