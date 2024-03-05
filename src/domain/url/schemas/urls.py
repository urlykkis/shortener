import secrets
from pydantic import BaseModel, Field


class ShortUrlModel(BaseModel):
    hash_id: str
    origin_url: str


class ShortResponse(BaseModel):
    hash_id: str
    origin_url: str
    is_active: bool
    full_url: str

    class Config:
        extra = "ignore"
