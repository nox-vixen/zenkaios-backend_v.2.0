from fastapi import APIRouter

from app.providers.moviebox.search import search
from app.providers.moviebox.mapper import map_subject

router = APIRouter()


@router.get("/api/search")
async def search_route(q: str):

    data = await search(q)

    results = []

    for item in data:
        subject = getattr(item, "subject", None)

        if subject:
            results.append(map_subject(subject))

    return {
        "results": results
    }