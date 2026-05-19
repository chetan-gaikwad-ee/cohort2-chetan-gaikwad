from datetime import datetime, timezone

from fastapi import APIRouter

from app.config import settings
from app.schemas.health import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health():
    return HealthResponse(
        status="ok",
        timestamp=datetime.now(timezone.utc),
        version=settings.APP_VERSION,
        environment=settings.ENVIRONMENT,
    )
