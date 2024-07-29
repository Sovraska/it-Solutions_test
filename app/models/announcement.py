from __future__ import annotations

from sqlalchemy import (Column, String, Integer)
from sqlalchemy.orm import Mapped

from app.core.db import Base


class Announcement(Base):
    title: Mapped[str] = Column(String(length=100), nullable=False)
    author: Mapped[str] = Column(String(length=100), nullable=False)
    views = Column(Integer)
    position = Column(Integer)

    def __repr__(self):
        return self.title

    class Config:
        orm_mode = True
