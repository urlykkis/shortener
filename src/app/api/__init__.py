from fastapi import APIRouter

from . import v1, redirect

router = APIRouter(prefix="/api", tags=["api"])
router.include_router(v1.router, prefix="/v1")
