from pydantic import BaseModel


class WebConfiguration(BaseModel):
    """Настройки для Web app"""
    HOST: str = "localhost"
    PORT: int = 8080
