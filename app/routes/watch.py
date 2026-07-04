from fastapi import APIRouter
from app.providers.moviebox.watch import get_watch

router = APIRouter()


@router.get("/watch")
async def watch(q: str):
    return await get_watch(q)