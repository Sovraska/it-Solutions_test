from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.crud.base import CRUDBase
from app.crud.hasher import Hasher
from app.models import User


class CRUDUser(CRUDBase):
    async def get(
        self,
        obj_id: int,
        session: AsyncSession,
    ):
        db_obj = await session.execute(
            select(self.model).where(self.model.id == obj_id).options(
                selectinload(User.examinations)
            )
        )
        return db_obj.scalars().first()

    async def update_id(
            self,
            db_obj,
            field: str,
            field_value: int,
            session: AsyncSession,
    ):
        # obj_data = jsonable_encoder(db_obj)
        setattr(db_obj, field, field_value)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def get_user_by_credentials(
            self,
            email,
            password,
            session: AsyncSession,
    ):
        db_obj = await session.execute(
            select(self.model).where(self.model.email == email)
        )
        res = db_obj.scalars().first()
        if not res:
            return None
        is_password_pass = Hasher.verify_password(
            password, hashed_password=res.hashed_password
        )

        if not is_password_pass:
            return None
        return res


user_crud = CRUDUser(User)
