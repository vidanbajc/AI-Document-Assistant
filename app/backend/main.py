from fastapi import FastAPI, Request, Form
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import StreamingResponse
from src.pipeline.rag_pipeline import RAGPipeline

app = FastAPI()
rag = RAGPipeline()
limiter = Limiter(key_func=get_remote_address)
templates = Jinja2Templates(directory="app/frontend/templates")

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/assistant")
def assistant(request: Request):
    return templates.TemplateResponse(request=request, name="assistant.html")

@app.post("/assistant")
@limiter.limit("25/minute")
async def get_answer(request: Request, question: str = Form(...)):
    return StreamingResponse(rag.query(question), media_type="text/plain")