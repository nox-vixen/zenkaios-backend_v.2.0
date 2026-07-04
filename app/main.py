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