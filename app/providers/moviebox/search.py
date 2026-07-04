from moviebox_api.v2 import Search, Session


async def search(query: str):
    session = Session()

    search = Search(
        session=session,
        query=query,
    )

    data = await search.get_content_model()

    return data.items