from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.announcement import Announcement


class CRUDUser(CRUDBase):
    async def get_top_ten(self, session: AsyncSession):
        db_obj = await session.execute(
            select(self.model).order_by(desc(self.model.views)).limit(10)
        )
        return db_obj.scalars().all()


announcement_crud = CRUDUser(Announcement)
