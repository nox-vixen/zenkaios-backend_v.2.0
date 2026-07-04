from moviebox_api.v1.stream import StreamFilesDetail
from moviebox_api.v2 import Session, Search, ItemDetails

session = Session()
search = Search(session)
details = ItemDetails(session)


async def get_watch(detail_path: str, season: int = 1, episode: int = 1):
    # Get complete details
    item = await details.get_content_model(detail_path)

    # Search again by title to obtain a SearchResultsItem
    results = await search.search(item.subject.title)

    target = None
    for result in results.items:
        if result.detailPath == detail_path:
            target = result
            break

    if target is None:
        raise Exception("MovieBox item not found")

    stream = StreamFilesDetail(session, target)
    data = await stream.get_modelled_content(season, episode)

    return {
        "streams": [
            {
                "resolution": s.resolutions,
                "codec": s.codecName,
                "format": s.format,
                "size": s.size,
                "url": str(s.url)
            }
            for s in data.streams
        ],
        "best": (
            {
                "resolution": data.best_stream_file.resolutions,
                "url": str(data.best_stream_file.url)
            }
            if data.best_stream_file
            else None
        )
    }