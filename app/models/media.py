from pydantic import BaseModel
from typing import Optional, Literal

MediaType = Literal[
    "anime",
    "movie",
    "tv",
    "donghua",
    "cartoon",
]


class MediaItem(BaseModel):
    id: str

    provider: str

    provider_id: str

    type: MediaType

    title: str

    original_title: Optional[str] = None

    description: Optional[str] = None

    poster: Optional[str] = None

    banner: Optional[str] = None

    backdrop: Optional[str] = None

    logo: Optional[str] = None

    year: Optional[int] = None

    rating: Optional[float] = None

    genres: list[str] = []

    language: Optional[str] = None

    country: Optional[str] = None

    status: Optional[str] = None

    episodes: Optional[int] = None

    duration: Optional[int] = None


class HomeResponse(BaseModel):
    featured: list[MediaItem] = []

    trending: list[MediaItem] = []

    popular: list[MediaItem] = []

    latest: list[MediaItem] = []

    top_rated: list[MediaItem] = []