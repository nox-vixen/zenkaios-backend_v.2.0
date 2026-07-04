from fastapi import APIRouter
import inspect
from moviebox_api.v2._bases import BaseDownloadableFilesDetail

router = APIRouter()

@router.get("/api/debug")
async def debug():
    return {
        "source": inspect.getsource(BaseDownloadableFilesDetail)
    }