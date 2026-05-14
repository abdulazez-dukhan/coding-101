
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Exercise 1 AI QA API")

# TODO 1:
# Create a Pydantic model called AskRequest with:
# - question: str
# - top_k: int = 3

class AskRequest(BaseModel):
    question: str
    top_k: int

# TODO 2:
# Create GET /health endpoint that returns {"status": "ok"}
@app.get("/")
def health():
    return {"status": "ok"}

# TODO 3:
# Create POST /ask endpoint.
# It should accept AskRequest and return:
# - question
# - answer
# - top_k
# - sources

@app.post("/Ask")
def fun(ret: AskRequest, sources:str, answer:str):
    return {f'question: {ret.question}',
            f'answer: {answer}',
            f'top_k: {ret.top_k}',
            f'source: {sources}'
    }
    

# Example fake answer:
# "This is a fake AI answer. In production, this would come from a RAG pipeline."
