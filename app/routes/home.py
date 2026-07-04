from fastapi import APIRouter

from app.providers.moviebox.home import get_homepage
from app.providers.moviebox.mapper import map_subject

router = APIRouter()


@router.get("/api/home")
async def home():

    homepage = await get_homepage()

    hero = []

    for section in homepage.operatingList:

        if section.type == "BANNER":

            for item in section.banner.items:

                subject = getattr(item, "subject", None)

                if subject is None:
                    continue

                hero.append(map_subject(subject))

            break

    return {
        "hero": hero
    }