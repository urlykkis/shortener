from sqlalchemy import select

from src.infrastructure.database.models import URL
from src.domain.base.interfaces.repository import SQLAlchemyRepository


class URLRepository(SQLAlchemyRepository):
    model = URL

    async def find_by_created(self, date):
        stmt = select(self.model).filter(self.model.created_at < date)
        res = await self.session.execute(stmt)
        return res.scalars()
