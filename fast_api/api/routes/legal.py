from fastapi import APIRouter, HTTPException
from agents.legal import get_legal_insights
from pydantic import BaseModel


class LegalQueryRequest(BaseModel):
    input_text: str

router = APIRouter()

@router.get("/")
async def get_insights(query: str):
    try:
        response = get_legal_insights(query)
        return {"success": True, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# POST method for structured queries with a JSON payload
@router.post("/query")
async def query_legal_insights(query: LegalQueryRequest):
    """
    Fetch market insights using a POST request with a JSON body.
    """
    try:
        response = get_legal_insights(query.input_text)
        return {"success": True, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
