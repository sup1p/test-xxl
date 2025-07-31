from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """Application settings."""

    PROJECT_NAME: str = "omar test"
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    DEBUG: bool = False

    SMTP_USER: str
    SMTP_HOST: str
    SMTP_PASS: str
    SMTP_PORT: int

    model_config = SettingsConfigDict(
        env_file=".env",
    )

settings = Settings()