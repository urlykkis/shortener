from fastapi import Request, Depends

from src.infrastructure.database.uow import UnitOfWork
from src.domain.url.usecase.url import URLService


async def uow_provider(request: Request) -> UnitOfWork:
    ...


async def uow(request: Request) -> UnitOfWork:
    uow = UnitOfWork(
        session=request.state.db_session
    )
    async with uow:
        return uow


def url_provider(request: Request) -> URLService:
    ...


def url_service(
        request: Request,
        uow=Depends(uow_provider),
) -> URLService:
    return URLService(uow)
