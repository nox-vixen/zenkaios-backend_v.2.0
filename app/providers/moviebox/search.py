import inspect
from moviebox_api.v2 import Session

async def search(query: str):
    return {
        "signature": str(inspect.signature(Session)),
        "methods": dir(Session),
    }