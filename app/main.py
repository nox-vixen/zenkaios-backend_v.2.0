from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.home import router as home_router
from app.routes.search import router as search_router
from app.routes.details import router as details_router

from app.routes.episodes import router as episodes_router

from app.routes.watch import router as watch_router



app = FastAPI(
    title="ZenkaiOS Backend",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

app.include_router(home_router)
app.include_router(search_router)
app.include_router(details_router)

app.include_router(episodes_router)

app.include_router(watch_router)


@app.get("/")
async def root():
    return {
        "name": "ZenkaiOS Backend",
        "version": "1.0.0",
        "status": "online",
        "providers": [
            {
                "id": "moviebox",
                "status": "enabled",
            }
        ],
    }


@app.get("/health")
async def health():
    return {
        "status": "ok",
    }


@app.get("/providers")
async def providers():
    return [
        {
            "id": "moviebox",
            "name": "MovieBox",
            "enabled": True,
        }
    ]


@app.get("/debug/moviebox")
async def debug_moviebox():
    try:
        from moviebox_api.v2 import Homepage

        homepage = Homepage()
        data = await homepage.get_content_model()

        return {
            "operatingList_type": str(type(data.operatingList)),
            "operatingList_length": len(data.operatingList),
            "platformList_type": str(type(data.platformList)),
            "platformList_length": len(data.platformList),
            "first_operating_item": (
                data.operatingList[0].model_dump()
                if data.operatingList
                else None
            ),
            "first_platform_item": (
                data.platformList[0].model_dump()
                if data.platformList
                else None
            ),
        }

    except Exception as e:
        return {
            "error": str(e),
        }