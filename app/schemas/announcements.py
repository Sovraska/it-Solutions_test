from pydantic import BaseModel


class AnnouncementRead(BaseModel):
    id: int
    title: str
    author: str
    views: int
    position: int
