from pathlib import Path

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.announcement import announcement_crud
from app.schemas.announcements import AnnouncementRead

router = APIRouter()

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent


@router.get(
    "/",
    response_model=list[AnnouncementRead],
)
async def get_top_ten_announcements(
        session: AsyncSession = Depends(get_async_session)
):
    result = await announcement_crud.get_top_ten(session=session)
    return result


@router.get(
    "/{obj_id}",
    response_model=AnnouncementRead,
    dependencies=[Depends(current_user)]
)
async def get_top_ten_announcements(
        obj_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    result = await announcement_crud.get(obj_id=obj_id, session=session)
    return result
