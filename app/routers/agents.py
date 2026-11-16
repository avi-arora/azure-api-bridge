import logging

from fastapi import APIRouter, HTTPException

from app.services.foundry import list_model_deployments

logger = logging.getLogger(__name__)
router = APIRouter(tags=["agents"])


@router.get("/agents")
async def get_agents():
    try:
        agents = await list_model_deployments()
    except Exception as exc:
        logger.exception("Failed to list deployments from Azure AI project")
        raise HTTPException(status_code=502, detail="Failed to fetch deployments") from exc
    return {"agents": agents}
