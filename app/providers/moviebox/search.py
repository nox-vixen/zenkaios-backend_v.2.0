from moviebox_api.v2 import Search


async def search(query: str):
    search = Search()
    return await search.search(query)