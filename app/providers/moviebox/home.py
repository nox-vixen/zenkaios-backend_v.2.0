from moviebox_api.v2 import Homepage


async def get_homepage():
    home = Homepage()

    data = await home.get_content_model()

    return data