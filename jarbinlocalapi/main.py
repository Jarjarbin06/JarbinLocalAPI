from fastapi import FastAPI
import uvicorn


jarbinlocalapi = FastAPI()


@jarbinlocalapi.get("/")
def get_root():
    """
        Route: `/`

        Get server status.
    """
    return {"status": "OK"}


def run() -> None:
    uvicorn.run(
        jarbinlocalapi,
        host="0.0.0.0",
        port=8000,
    )

from jarbinlocalapi.app import main
from jarbinlocalapi.api import main
