from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from chatbot import get_bot_reply
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class Message(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
def chat_api(msg: Message):
    reply = get_bot_reply(msg.message)
    return {"reply": reply}

if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)
