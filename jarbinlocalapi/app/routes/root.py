from fastapi.responses import HTMLResponse

from jarbinlocalapi.app import app
from jarbinlocalapi.app.templates.root import template_root
from jarbinlocalapi import (
    __name__ as title,
    __version__ as version
)


@app.get("/", response_class=HTMLResponse)
async def get_root():
    """
        Route: `/app`

        Return base "Hello World!" page.
    """

    return template_root.render(title = title, version = version)
