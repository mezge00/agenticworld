from fastapi import Depends, HTTPException, Security
from sqlalchemy.orm import Session
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseSettings
from utils.db_setup import get_db
from utils.gemini_wrapper import configure_gemini_model

# Settings class to fetch configuration
class Settings(BaseSettings):
    app_name: str = "My AI Backend"
    api_key: str
    database_url: str

    class Config:
        env_file = ".env"

# Dependency for fetching configuration
def get_settings() -> Settings:
    return Settings()

# Dependency for database connection
def get_database_connection() -> Session:
    db = get_db()
    try:
        yield db
    finally:
        db.close()

# Dependency for API Key validation
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=True)

async def verify_api_key(api_key: str = Depends(api_key_header), settings: Settings = Depends(get_settings)):
    if api_key != settings.api_key:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

# Dependency for Google Generative AI
def get_generative_model() -> GenerativeModel:
    return configure_gemini_model()
