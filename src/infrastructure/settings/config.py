from functools import lru_cache

from src.infrastructure.settings.configurations import \
    GlobalSettings, DatabaseConfiguration, WebConfiguration


class Config(GlobalSettings):
    """Конфиг"""
    web: WebConfiguration
    database: DatabaseConfiguration


@lru_cache
def load_config(env_file: str = ".env") -> "Config":
    """Загрузка конфига"""
    return Config(_env_file=env_file)
