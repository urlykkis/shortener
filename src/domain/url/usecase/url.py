import secrets

from src.domain.base.interfaces.uow import IUnitOfWork
from src.domain.url.dto.url import FullUrlDTO
from src.infrastructure.database.models.urls import URL
from src.domain.url.schemas import ShortUrlModel


import random
import string


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


class URLService:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def get_url(self, hash_id: str) -> FullUrlDTO:
        url = await self.uow.url.find_one(hash_id=hash_id)
        return FullUrlDTO(**url.as_dict())

    async def short_url(self, url: str):
        url = await self.uow.url.add_one(
            ShortUrlModel(hash_id=generate_random_string(7), origin_url=url).model_dump()
        )
        return url
