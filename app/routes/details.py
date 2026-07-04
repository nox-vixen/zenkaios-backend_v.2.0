from fastapi import APIRouter
import inspect
from moviebox_api.v2 import ItemDetails

router = APIRouter()


@router.get("/debug/details")
async def debug_details():

    return {
        "get_content_model": str(inspect.signature(ItemDetails.get_content_model)),
        "get_content": str(inspect.signature(ItemDetails.get_content)),
    }