from pathlib import Path
from fastapi import FastAPI, Request
from os.path import join
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException
from jinja2 import Environment, FileSystemLoader
import uvicorn

from jarbinlocalapi import (
    __name__ as title,
    __version__ as version,
)


JARBINLOCALAPI_DIR = Path(__file__).resolve().parent

STATIC_DIR = JARBINLOCALAPI_DIR / "app" / "static"


jarbinlocalapi = FastAPI()


jarbinlocalapi.mount(
    "/app/static",
    StaticFiles(directory=STATIC_DIR),
    name="static",
)


templates = Environment(
    loader=FileSystemLoader(join(STATIC_DIR, "html"))
)


@jarbinlocalapi.exception_handler(StarletteHTTPException)
async def not_found_handler(
        request: Request,
        exc: StarletteHTTPException,
    ):
    if exc.status_code == 404:
        template = templates.get_template("404.html")

        content = template.render(
            title=title,
            version=version,
            path=request.url.path,
        )

        return HTMLResponse(
            content=content,
            status_code=404,
        )

    return HTMLResponse(
        content=exc.detail,
        status_code=exc.status_code,
    )


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
from jarbinlocalapi.updater import main
