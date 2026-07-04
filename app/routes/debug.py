from fastapi import APIRouter
from moviebox_api.v2 import TVSeriesDetails, Session

router = APIRouter()

session = Session()
tv = TVSeriesDetails(session)

@router.get("/api/debug")
async def debug():
    return {
        "methods": [m for m in dir(tv) if not m.startswith("_")]
    }