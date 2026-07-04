from fastapi import APIRouter

from app.providers.moviebox.details import get_details

router = APIRouter()


@router.get("/api/details/{detail_path}")
async def details(detail_path: str):
    data = await get_details(detail_path)

    return data.model_dump()