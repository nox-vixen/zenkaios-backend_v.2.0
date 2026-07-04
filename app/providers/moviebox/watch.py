from moviebox_api.v2 import Search, ItemDetails
from moviebox_api.v2.requests import Session

session = Session()


async def get_watch(query: str):
    search = Search(
        session=session,
        query=query
    )

    results = await search.get_content_model()

    if not results.items:
        return {
            "success": False,
            "message": "Nothing found"
        }

    item = results.first_item

    details = ItemDetails(session)

    detail = await details.get_content_model(item)

    return {
        "success": True,
        "item": item,
        "detail": detail
    }