from fastapi import APIRouter
import inspect
from moviebox_api.v2 import TVSeriesDetails

router = APIRouter()

@router.get("/api/debug")
async def debug():
    return {
        "source": inspect.getsource(TVSeriesDetails)
    }