from pathlib import Path
from starlette.responses import JSONResponse
from fastapi import Request
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader
from os.path import join

from jarbinlocalapi import (
    __name__ as title,
    __version__ as version,
)
from jarbinlocalapi.main import jarbinlocalapi


STATIC_DIR = Path(__file__).resolve().parent.parent.parent / "app" / "static"


templates = Environment(
    loader=FileSystemLoader(join(STATIC_DIR, "html"))
)

class SystemInfoError(Exception):
    pass


@jarbinlocalapi.exception_handler(SystemInfoError)
async def system_error_handler(
        request: Request,
        exc: SystemInfoError,
    ):
    if request.url.path.startswith("/app"):
        template = templates.get_template("505.html")

        content = template.render(
            title=title,
            version=version,
            path=request.url.path,
        )

        return HTMLResponse(
            content=content,
            status_code=500,
        )

    return JSONResponse(
        content={"detail": "Internal Server Error"},
        status_code=500,
    )
