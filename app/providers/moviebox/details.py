from moviebox_api.v2 import ItemDetails, Session


async def get_details(detail_path: str):
    session = Session()

    details = ItemDetails(session)

    return await details.get_content_model(detail_path)