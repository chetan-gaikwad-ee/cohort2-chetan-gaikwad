import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings
from app.logging_config import setup_logging
from app.middleware.logging_middleware import RequestLoggingMiddleware
from app.routes import health

setup_logging()

logger = logging.getLogger("app.startup")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(
        "Application started",
        extra={
            "app_version": settings.APP_VERSION,
            "environment": settings.ENVIRONMENT,
        },
    )
    yield
    logger.info("Application shutdown")


app = FastAPI(lifespan=lifespan)

app.add_middleware(RequestLoggingMiddleware)
app.include_router(health.router)
