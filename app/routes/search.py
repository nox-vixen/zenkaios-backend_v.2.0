from fastapi import APIRouter

from app.providers.moviebox.search import search
from app.providers.moviebox.mapper import map_subject

router = APIRouter()


@router.get("/api/search")
async def search_route(q: str):

    items = await search(q)

    results = []

    for subject in items:
        results.append(map_subject(subject))

    return {
        "results": results
    }