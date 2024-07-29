from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    username: str

    class Config:
        from_attributes = True


class UserCreate(schemas.BaseUserCreate):
    username: str


class UserUpdate(schemas.BaseUserUpdate):
    username: Optional[str]
