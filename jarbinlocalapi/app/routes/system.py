from fastapi.responses import HTMLResponse
from httpx import AsyncClient

from jarbinlocalapi.app import app
from jarbinlocalapi.app.templates.system import (
    template_overview,
    template_cpu,
    template_memory
)
from jarbinlocalapi import (
    __name__ as title,
    __version__ as version
)


@app.get("/system", response_class=HTMLResponse)
async def get_system():
    """
        Route: `/app/system`

        Return overview system page.
    """

    async with AsyncClient() as client:
        response = await client.get("http://jarjarbin.local/api/system")

    return template_overview.render(title = title, version = version, system = response.json())


@app.get("/system/cpu", response_class=HTMLResponse)
async def get_system():
    """
        Route: `/app/system/cpu`

        Return cpu system page.
    """

    async with AsyncClient() as client:
        response = await client.get("http://jarjarbin.local/api/system/cpu")

    return template_cpu.render(title = title, version = version, cpu = response.json())


@app.get("/system/memory", response_class=HTMLResponse)
async def get_system():
    """
        Route: `/app/system/memory`

        Return memory system page.
    """

    async with AsyncClient() as client:
        response = await client.get("http://jarjarbin.local/api/system/memory")

    return template_memory.render(title = title, version = version, memory = response.json())
