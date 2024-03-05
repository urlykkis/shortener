from src.infrastructure.database.models import Settings
from src.domain.base.interfaces.repository import SQLAlchemyRepository


class SettingsRepository(SQLAlchemyRepository):
    model = Settings
