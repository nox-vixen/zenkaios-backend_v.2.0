from fastapi import APIRouter

from app.providers.moviebox.watch import get_watch

router = APIRouter(prefix="/api/watch", tags=["watch"])


@router.get("")
async def watch(
    detailPath: str,
    season: int = 1,
    episode: int = 1,
):
    return await get_watch(detailPath, season, episode)