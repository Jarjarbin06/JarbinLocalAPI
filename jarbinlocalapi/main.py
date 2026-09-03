from fastapi import FastAPI, APIRouter
import uvicorn


jarbinlocalapi = FastAPI()

app = APIRouter(prefix="/app")
api = APIRouter(prefix="/api")

jarbinlocalapi.include_router(app)
jarbinlocalapi.include_router(api)


@jarbinlocalapi.get("/")
def get_root():
    """
        Route: `/`

        Get server status
    """
    return {"status": "ok"}


def run() -> None:
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
    )


from jarbinlocalapi.api.routes import (
    root
)
from jarbinlocalapi.app.routes import (
    root
)
