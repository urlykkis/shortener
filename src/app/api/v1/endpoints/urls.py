import logging

from fastapi import APIRouter, Depends, Request, Body
from pydantic import HttpUrl

from src.app.api import providers
from src.domain.url.usecase.url import URLService
from src.domain.url.schemas import ShortResponse
from src.infrastructure.database.models import Settings
from src.infrastructure.database.uow import UnitOfWork

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/short", response_model=ShortResponse)
async def short_url(
        request: Request,
        url_service: URLService = Depends(providers.url_provider),
        uow: UnitOfWork = Depends(providers.uow_provider),
        url: HttpUrl = Body(..., embed=True)
):
    url = await url_service.short_url(str(url))
    await url_service.uow.commit()
    settings = await uow.settings.find_one(id=1)
    logger.info(f"Created: {url.hash_id} -> {url.origin_url}")

    response = url.as_dict()
    response["full_url"] = f"{settings.host}/{url.hash_id}"

    return ShortResponse(
        **response
    )
