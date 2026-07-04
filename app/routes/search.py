from fastapi import APIRouter

from app.providers.moviebox.search import search

router = APIRouter()


@router.get("/api/search")
async def search_route(q: str):

    data = await search(q)

    return {
        "type": str(type(data)),
        "dir": dir(data),
        "repr": str(data)[:5000],
    }