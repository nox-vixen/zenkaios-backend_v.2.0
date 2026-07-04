from fastapi import APIRouter
import inspect
import moviebox_api.v2 as mb

router = APIRouter()


@router.get("/debug/details")
async def debug_details():
    return {
        "exports": dir(mb),
    }