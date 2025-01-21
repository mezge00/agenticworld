from pydantic import BaseSettings, Field
from typing import Optional

class Settings(BaseSettings):
    # General App Settings
    app_name: str = Field(default="My AI Backend", description="The name of the application.")
    debug: bool = Field(default=False, description="Enable or disable debug mode.")

    # Database Configuration
    database_url: str = Field(..., description="The URL for the database connection.")

    # API Keys
    gemini_api_key: str = Field(..., description="API key for Google Gemini Generative AI.")
    secret_key: str = Field(..., description="Secret key for secure operations.")

    # Third-party Services
    redis_url: Optional[str] = Field(default=None, description="URL for Redis caching service.")
    s3_bucket_name: Optional[str] = Field(default=None, description="S3 bucket for file storage.")

    # Environment Configuration
    environment: str = Field(default="development", description="Environment (development, testing, production).")

    # Pydantic Configuration
    class Config:
        env_file = ".env"  # Automatically load settings from .env file
        env_file_encoding = "utf-8"
        case_sensitive = True  # Make environment variables case-sensitive

# Instantiate settings
settings = Settings()
