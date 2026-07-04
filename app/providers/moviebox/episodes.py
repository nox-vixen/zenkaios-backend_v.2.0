from app.providers.moviebox.client import session


async def get_episodes(detail_path: str):
    return {
        "detailPath": detail_path,
        "message": "Episodes endpoint not implemented yet."
    }