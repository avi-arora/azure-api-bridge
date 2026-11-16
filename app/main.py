from fastapi import FastAPI

from app.routers import agents, token

app = FastAPI(title="VeritlexAI Azure API Bridge", version="0.1.0")

app.include_router(agents.router)
app.include_router(token.router)


@app.get("/health", tags=["health"])
async def health():
    return {"status": "ok"}
