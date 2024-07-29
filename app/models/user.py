from __future__ import annotations

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped

from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    username: Mapped[str] = Column(String(length=100), nullable=False)

    def __repr__(self):
        return self.username
