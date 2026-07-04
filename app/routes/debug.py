from fastapi import APIRouter

from app.providers.moviebox.session import session
from moviebox_api.v2 import TVSeriesDetails

router = APIRouter()


@router.get("/debug/watch/{detail_path}")
async def debug_watch(detail_path: str):

    api = TVSeriesDetails(session)

    data = await api.get_content_model(detail_path)

    return data.model_dump()