from app.providers.moviebox.client import client


async def get_episodes(
    detail_path: str,
    season: int = 1,
):
    """
    Returns all episodes for a MovieBox title.
    """

    response = await client.get(
        "/subject/episode/list",
        params={
            "detailPath": detail_path,
            "season": season,
        },
    )

    return response.json()