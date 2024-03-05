from datetime import datetime
from enum import Enum
from typing import List, Optional

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pydantic import BaseModel, Field

import uvicorn

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationException
from fastapi.responses import JSONResponse

from src.app.api import providers
from src.app.api import router, redirect
from src.infrastructure.tasks.cleanup import cleanup_urls

app = FastAPI(
    title="Shortener URL"
)

app.dependency_overrides[providers.uow_provider] = providers.uow
app.dependency_overrides[providers.url_provider] = providers.url_service

app.include_router(router)
app.include_router(redirect.router)


@app.exception_handler(ValidationException)
async def validation_exception_handler(request: Request, exc: ValidationException):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


@app.on_event("startup")
async def on_startup():
    job_defaults = dict(coalesce=False, max_instances=3)

    scheduler = AsyncIOScheduler(
        timezone="UTC", job_defaults=job_defaults
    )
    scheduler.add_job(
        func=cleanup_urls,
        trigger="cron",
        # trigger="interval",
        hour=0,
        # seconds=1,
        id="cleanup_urls",
        name="cleanup_urls",
        replace_existing=True
    )
    scheduler.start()

if __name__ == "__main__":
    uvicorn.run(app=app)
