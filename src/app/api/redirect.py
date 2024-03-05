import logging

from fastapi import APIRouter, Depends, Query
from fastapi.responses import Response, RedirectResponse, JSONResponse

from src.app.api import providers
from src.domain.url.usecase.url import URLService

router = APIRouter(tags=["redirect"])
logger = logging.getLogger(__name__)


@router.get("/{hash_id}")
async def forward_to_origin(
        hash_id: str,
        url_service: URLService = Depends(providers.url_provider)

):
    url = await url_service.get_url(hash_id=hash_id)

    if not url:
        return Response(status_code=404)

    logger.info(f"Redirected: {url.hash_id} -> {url.origin_url}")

    return RedirectResponse(url=url.origin_url)
