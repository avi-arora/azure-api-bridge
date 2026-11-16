import os
from dataclasses import dataclass
from functools import lru_cache


@dataclass(frozen=True)
class Settings:
    ai_project_endpoint: str
    mobile_model_deployment_url: str | None
    model_api_version: str | None


@lru_cache
def get_settings() -> Settings:
    return Settings(
        ai_project_endpoint=os.getenv("AZURE_AI_PROJECT_ENDPOINT", ""),
        mobile_model_deployment_url=os.getenv("MOBILE_MODEL_DEPLOYMENT_URL"),
        model_api_version=os.getenv("MODEL_API_VERSION"),
    )
