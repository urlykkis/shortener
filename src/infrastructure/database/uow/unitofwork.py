from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.repositories.url import URLRepository
from src.infrastructure.database.repositories.settings import SettingsRepository


class UnitOfWork:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def __aenter__(self):
        self.url = URLRepository(self.session)
        self.settings = SettingsRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
