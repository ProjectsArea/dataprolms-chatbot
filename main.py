from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import cohere

app = FastAPI()

# Mount static files and templates
templates = Jinja2Templates(directory="templates") 

# Initialize Cohere client with your one trial API key
co = cohere.Client("W0ZMiF8D4eU3eMGgZevXJMPwnJMzJVtd7JYwvo0V")  # Replace with your real key

@app.get("/", response_class=HTMLResponse)
async def serve_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")

    response = co.chat(
        model="command-r",  # Trial users can access this
        message=user_message,
        temperature=0.7,
        max_tokens=500
    )

    return JSONResponse({"response": response.text})
