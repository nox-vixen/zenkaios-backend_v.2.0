from moviebox_api.v2 import Search, Session


async def search(query: str):
    session = Session()

    search = Search(
        session=session,
        query=query,
    )

    data = await search.get_content_model()

    return {
        "items_type": str(type(data.items)),
        "items_length": len(data.items),
        "first_item": (
            data.items[0].model_dump()
            if data.items
            else None
        ),
    }