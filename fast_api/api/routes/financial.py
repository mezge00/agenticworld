from fastapi import APIRouter, HTTPException, Query, Body
from pydantic import BaseModel
from agents.financial import get_financial_insights

router = APIRouter()

class FinancialQuery(BaseModel):
    input_text: str

@router.get("/")
async def get_financial_data(query: str = Query(...)):
    """
    Handles GET requests for financial insights queries.
    """
    try:
        response = get_financial_insights(query)
        return {"success": True, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/query")
async def query_financial_agent(query: FinancialQuery):
    """
    Handles POST requests for financial insights queries.
    """
    try:
        response = get_financial_insights(query.input_text)
        return {"success": True, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
