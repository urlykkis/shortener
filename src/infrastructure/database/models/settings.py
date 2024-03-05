from datetime import datetime

from sqlalchemy import (String, Integer, DateTime, func, Boolean)
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.database.models.base import Base


class Settings(Base):
    __tablename__ = "settings"

    id: Mapped[int] = mapped_column(
        Integer, nullable=False, index=True, primary_key=True
    )

    domain: Mapped[str] = mapped_column(
        String(32), nullable=False, default="localhost:3000"
    )

    @property
    def host(self):
        if "localhost" in self.domain:
            return f"http://{self.domain}"

        return f"https://{self.domain}"
