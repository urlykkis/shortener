import os
import uvicorn

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

from src.infrastructure.settings import Config, load_config
from src.infrastructure.database.connection import create_async_session

from src.app.app import app as main_app
from src.app.middleware.db_session import DatabaseSessionMiddleware
from src.infrastructure.tasks.cleanup import cleanup_urls
from src.infrastructure.logging.logger import logger, setup_logger


def main():
    setup_logger("INFO")
    env_file = os.getenv("ENV_FILE", ".env")
    config: Config = load_config(env_file)

    session_factory = create_async_session(str(config.database.dsn))
    main_app.add_middleware(
        DatabaseSessionMiddleware,
        session_factory=session_factory
    )
    uvicorn.run(app=main_app, host=config.web.HOST, port=config.web.PORT)


if __name__ == '__main__':
    main()
