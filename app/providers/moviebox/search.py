from moviebox_api.v2 import Search, Session


async def search(query: str):
    session = Session()

    search = Search(
        session=session,
        query=query,
    )

    try:
        data = await search.get_content_model()

        return {
            "type": str(type(data)),
            "attributes": dir(data),
        }

    except Exception as e:
        return {
            "error": str(e),
        }