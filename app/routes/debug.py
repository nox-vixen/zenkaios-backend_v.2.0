from fastapi import APIRouter
import inspect
from moviebox_api.v2._bases import BaseItemDetails

router = APIRouter()

@router.get("/api/debug")
async def debug():
    return {
        "source": inspect.getsource(BaseItemDetails)
    }