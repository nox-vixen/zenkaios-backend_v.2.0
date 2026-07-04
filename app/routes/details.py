from fastapi import APIRouter
import inspect
from moviebox_api.v2 import ItemDetails

router = APIRouter()


@router.get("/debug/details")
async def debug_details():
    return {
        "signature": str(inspect.signature(ItemDetails)),
        "methods": [
            m for m in dir(ItemDetails)
            if not m.startswith("__")
        ]
    }