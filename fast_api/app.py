from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from  fast_api.api.routes.financial import router as financial_router
from fast_api.api.routes.healthcare import router as healthcare_router
from  fast_api.api.routes.market_insights import router as market_insight_router
from  fast_api.api.routes.legal import router as legal_router
from  fast_api.api.routes.education import router as education_router

import sys
import os

# Add the "backend" directory to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Create FastAPI app
app = FastAPI()

# Configure CORS (important for connecting frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend's URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(financial_router, prefix="/financial", tags=["financial"])
app.include_router(healthcare_router, prefix="/healthcare", tags=["healthcare"])
app.include_router(education_router, prefix="/education", tags=["education"])
app.include_router(legal_router, prefix="/legal", tags=["legal"])
app.include_router(market_insight_router, prefix="/market", tags=["market"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app:app",  # Path to the app object in the `app.py` module
        host="0.0.0.0",  # Change to "127.0.0.1" if you want to restrict it to localhost
        port=5000,        # Port to run the app on
        reload=True       # Enable auto-reload for development
    )
