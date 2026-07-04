from fastapi import APIRouter

from app.providers.moviebox.episodes import get_episodes

router = APIRouter()


@router.get("/api/episodes/{detail_path}")
async def episodes(
    detail_path: str,
    season: int = 1,
):
    return await get_episodes(detail_path, season)