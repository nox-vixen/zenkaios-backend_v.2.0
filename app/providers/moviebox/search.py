import inspect
from moviebox_api.v2 import Search


async def search(query: str):
    return {
        "signature": str(inspect.signature(Search)),
        "methods": dir(Search),
    }