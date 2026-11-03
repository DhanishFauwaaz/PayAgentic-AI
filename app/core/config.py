import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App Settings
    PROJECT_NAME: str = "PayAgentic-AI"
    VERSION: str = "1.0.0"
    
    # Redis URL
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")

    # PayPal API credentials
    PAYPAL_CLIENT_ID: str = os.getenv("PAYPAL_CLIENT_ID", "sandbox_client_id_placeholder")
    PAYPAL_CLIENT_SECRET: str = os.getenv("PAYPAL_CLIENT_SECRET", "sandbox_client_secret_placeholder")

    # AI Model / Llama credentials (with safe defaults)
    LLAMA_API_KEY: str = os.getenv("LLAMA_API_KEY", "dummy_llama_key")
    MODEL_API_KEY: str = os.getenv("MODEL_API_KEY", "dummy_model_key")
    META_TEAM_ID: str = os.getenv("META_TEAM_ID", "dummy_team_id")
    META_PROJECT_ID: str = os.getenv("META_PROJECT_ID", "dummy_project_id")

    class Config:
        env_file = ".env"
        extra = "ignore"  # Ignores extra fields without crashing

settings = Settings()