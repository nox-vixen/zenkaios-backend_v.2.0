from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
        import inspect
        from moviebox_api.v2 import Homepage

        return {
            "signature": str(inspect.signature(Homepage)),
            "methods": [
                m
                for m in dir(Homepage)
                if not m.startswith("_")
            ],
        }

    except Exception as e:
        return {
            "error": str(e),
        }