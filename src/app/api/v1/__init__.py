from fastapi import APIRouter
from .endpoints import urls


router = APIRouter()
router.include_router(urls.router, prefix="/urls")
