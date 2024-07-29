from pathlib import Path

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.api.routers import main_router
from app.core.config import settings

app = FastAPI(title=settings.app_title)

app.include_router(main_router)

BASE_DIR = Path(__file__).resolve(strict=True).parent

