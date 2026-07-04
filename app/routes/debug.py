from fastapi import APIRouter
from app.providers.moviebox.details import details

router = APIRouter()

@router.get("/api/debug/{detail_path}")
async def debug(detail_path: str):
    data = await details.get_content_model(detail_path)

    return {
        "type": str(type(data)),
        "attributes": dir(data)
    }