from app.config import get_settings
from app.services.credentials import get_credential

COGNITIVE_SERVICES_SCOPE = "https://cognitiveservices.azure.com/.default"


async def get_openai_token() -> dict[str, str | None]:
    settings = get_settings()
    token = await get_credential().get_token(COGNITIVE_SERVICES_SCOPE)
    return {
        "token": token.token,
        "endpoint": settings.mobile_model_deployment_url,
        "version": settings.model_api_version,
    }

