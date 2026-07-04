from fastapi import APIRouter
import moviebox_api.v2 as m

router = APIRouter()

@router.get("/api/debug")
async def debug():
    return {
        "members": dir(m)
    }