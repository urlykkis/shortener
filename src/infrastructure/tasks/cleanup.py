import os
from datetime import datetime, timedelta

from src.infrastructure.database.models import URL
from src.infrastructure.settings.config import load_config
from src.infrastructure.database.connection import create_async_session
from src.infrastructure.database.uow.unitofwork import UnitOfWork
from src.infrastructure.logging.logger import logger


async def cleanup_urls(
        days: int = 1,
):
    logger.info("Start cleanup URL's")
    env_file = os.getenv("ENV_FILE", ".env")
    config = load_config(env_file)
    pool = create_async_session(url=str(config.database.dsn))

    async with pool() as session:
        uow = UnitOfWork(session=session)
        now = datetime.now()

        cleanup_date = now - timedelta(days=days)

        async with uow:
            urls_to_delete = await uow.url.find_by_created(cleanup_date)

            for url in urls_to_delete:
                await uow.session.delete(url)

            await uow.commit()
