from typing import Any

from azure.ai.projects.aio import AIProjectClient

from app.config import get_settings
from app.services.credentials import get_credential


async def list_model_deployments() -> list[dict[str, Any]]:
    """List model deployments in the Azure AI Foundry project, shaped as agent records."""
    endpoint = get_settings().ai_project_endpoint
    if not endpoint:
        raise RuntimeError("AZURE_AI_PROJECT_ENDPOINT is not configured")

    results: list[dict[str, Any]] = []
    async with AIProjectClient(endpoint=endpoint, credential=get_credential()) as client:
        async for dep in client.deployments.list():
            model_name = getattr(dep, "model_name", None)
            results.append(
                {
                    "id": dep.name,
                    "model": model_name,
                    "type": "deployment",
                    "agent_id": model_name,
                    "default": False,
                    "recommended": False,
                }
            )
    return results
