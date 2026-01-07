from functools import lru_cache
from pydantic import BaseSettings
from app.config.env import get_env, Environment


class Settings(BaseSettings):
    app_name: str = "__PROJECT_NAME__"
    env: Environment = get_env()

    log_level: str = "INFO"

    database_url: str | None = None
    s3_bucket: str | None = None

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache
def settings() -> Settings:
    return Settings()
