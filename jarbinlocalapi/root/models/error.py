from starlette.responses import JSONResponse
from fastapi import Request
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader
from os.path import join
from starlette.exceptions import HTTPException as StarletteHTTPException

from jarbinlocalapi import (
    __name__ as title,
    __version__ as version,
)
from jarbinlocalapi.root import jarbinlocalapi, STATIC_DIR

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
        template = templates.get_template("500.html")

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
