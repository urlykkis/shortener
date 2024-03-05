from datetime import datetime

from sqlalchemy import (String, Integer, DateTime, func, Boolean)
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.database.models.base import Base


class URL(Base):
    __tablename__ = "urls"

    hash_id: Mapped[str] = mapped_column(
        String(7), nullable=False, unique=True, index=True, primary_key=True
    )
    origin_url: Mapped[str] = mapped_column(
        String(256), nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean(),
        nullable=False,
        default=True,
        server_default='true'
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(),
        nullable=False,
        server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(),
        onupdate=func.now,
        nullable=True
    )
