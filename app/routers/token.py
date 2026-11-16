import logging

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from app.services.tokens import get_openai_token

logger = logging.getLogger(__name__)
router = APIRouter(tags=["token"])


@router.get("/ai/token")
async def get_ai_token():
    try:
        openai_token = await get_openai_token()
    except Exception as exc:
        logger.exception("Failed to acquire Azure OpenAI token")
        raise HTTPException(status_code=502, detail="Failed to acquire token") from exc

    return JSONResponse(
        status_code=200,
        content={
            "data": True,
            "message": "VeritlexAI token fetched successfully",
            "token": openai_token["token"],
            "endpoint": openai_token["endpoint"],
            "version": openai_token["version"],
        },
    )
