
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Minimal FastAPI App",
    description="A tiny FastAPI app for AI engineering exercises.",
    version="0.1.0",
)

class EchoRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/echo")
def echo(request: EchoRequest):
    return {
        "original_text": request.text,
        "uppercase_text": request.text.upper(),
        "length": len(request.text),
    }
