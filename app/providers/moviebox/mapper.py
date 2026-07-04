def map_subject(subject):
    return {
        "id": str(subject.subjectId),
        "title": subject.title,
        "poster": subject.cover.url if subject.cover else None,
        "rating": subject.imdbRatingValue,
        "year": (
    str(subject.releaseDate.year)
    if subject.releaseDate
    else None
),
        "genres": subject.genre,
        "country": subject.countryName,
        "type": subject.subjectType,
        "detailPath": subject.detailPath,
    }