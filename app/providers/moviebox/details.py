from moviebox_api.v2 import ItemDetails, Session

session = Session()
details = ItemDetails(session)


async def get_details(path: str):
    data = details.get_content_model(path)

    subject = data.subject
    resource = data.resource

    return {
        "id": subject.subjectId,
        "title": subject.title,
        "description": subject.description,
        "poster": str(subject.cover.url),
        "rating": subject.imdbRatingValue,
        "year": subject.releaseDate.year if subject.releaseDate else None,
        "genres": subject.genre,
        "country": subject.countryName,
        "trailer": (
            subject.trailer.videoAddress.url
            if subject.trailer
            else None
        ),
        "dubs": [
            {
                "language": d.lanName,
                "detailPath": d.detailPath
            }
            for d in subject.dubs
        ],
        "cast": [
            {
                "name": s.name,
                "role": s.character
            }
            for s in data.stars[:20]
        ],
        "resource": {
            "source": resource.source if resource else None,
            "seasons": (
                [
                    {
                        "season": s.se,
                        "episodes": s.maxEp,
                        "qualities": [
                            r.resolution
                            for r in s.resolutions
                        ]
                    }
                    for s in resource.seasons
                ]
                if resource
                else []
            )
        }
    }