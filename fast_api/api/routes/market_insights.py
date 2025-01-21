import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from agents.market_insights import get_market_insights

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

router = APIRouter()

# Define the request model for POST requests
class MarketQueryRequest(BaseModel):
    input_text: str

# GET method for quick query via query parameters
@router.get("/")
async def get_insights(query: str):
    """
    Fetch market insights using a GET request with query parameters.
    """
    try:
        response = get_market_insights(query)
        {"success": True, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# POST method for structured queries with a JSON payload
@router.post("/query")
async def query_market_insights(query: MarketQueryRequest):
    """
    Fetch market insights using a POST request with a JSON body.
    """
    try:
        response = get_market_insights(query.input_text)
        return {"success": True, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
