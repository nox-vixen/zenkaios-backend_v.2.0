from moviebox_api.v2 import Details


async def get_details(detail_path: str):
    details = Details(detail_path)
    return await details.get_content_model()