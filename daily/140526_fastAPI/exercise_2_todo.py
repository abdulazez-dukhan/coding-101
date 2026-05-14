
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field, ValidationError

app = FastAPI(title="Exercise 2 Retrieval API")

FAKE_CHUNKS = [
    {
        "text": "RAG retrieves relevant chunks before generation.",
        "source": "rag_notes.md",
        "score": 0.92,
    },
    {
        "text": "Vector databases store embeddings and metadata payloads.",
        "source": "qdrant_notes.md",
        "score": 0.88,
    },
    {
        "text": "FastAPI exposes AI functionality through HTTP endpoints.",
        "source": "fastapi_notes.md",
        "score": 0.84,
    },
]

# TODO 1:
# Create SearchRequest model with:
# - query: str
# - top_k: int = 3
# - source_filter: Optional[str] = None
class SearchRequest(BaseModel):
    query: str = Field(
        min_length=3
    )
    top_k: int = Field(
        le=10,
        ge=3
    )
    source_filter: Optional[str]=None

# TODO 2:
# Create POST /search endpoint.
# It should:
# - filter FAKE_CHUNKS by source if source_filter is provided
# - return only top_k results
# - include query and top_k in response
@app.post("/search")
def search(request:SearchRequest):
    try:
        if request.source_filter:
            print(not request.source_filter)
            filter = [x for x in FAKE_CHUNKS if (x["source"] == request.source_filter)]

            return{
                "query": request.query,
                "top_k": request.top_k,
                "source_filter": filter
            }
        else:
            return{
                "query": request.query,
                "top_k": request.top_k,
            }
    except ValidationError:
        return{"results": 404}

# TODO 3:
# Add validation with Field:
# - query minimum length 3
# - top_k between 1 and 10