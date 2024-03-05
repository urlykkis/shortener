from typing import Optional

from pydantic import BaseModel, Field
from datetime import datetime

from src.domain.base.dto.base import BaseDTO


class UrlDTO(BaseDTO):
    hash_id: str
    origin_url: str
    is_active: bool


class FullUrlDTO(UrlDTO):
    created_at: datetime
    updated_at: datetime | None
