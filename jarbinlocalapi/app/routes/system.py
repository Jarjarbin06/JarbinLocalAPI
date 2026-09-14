from fastapi.responses import HTMLResponse
from httpx import AsyncClient

from jarbinlocalapi.app import app
from jarbinlocalapi.templates.app.system import (
    template_overview,
    template_cpu,
    template_memory,
    template_battery,
    template_disk,
    template_network,
    template_processes,
    template_system,
    template_temperatures,
    template_top_processes
)
from jarbinlocalapi import (
    __name__ as title,
    __version__ as version
)


@app.get("/system", response_class=HTMLResponse)
async def get_app_system():
    """
        Route: `/app/system`

        Return overview system page.
    """

    async with AsyncClient() as client:
        response = await client.get("http://jarjarbin.local/api/system")

    return template_overview.render(title = title, version = version, system = response.json()["data"])


@app.get("/system/cpu", response_class=HTMLResponse)
async def get_app_system_cpu():
    """
        Route: `/app/system/cpu`

        Return cpu system page.
    """

    async with AsyncClient() as client:
        response = await client.get("http://jarjarbin.local/api/system/cpu")

    return template_cpu.render(title = title, version = version, cpu = response.json()["data"])


@app.get("/system/memory", response_class=HTMLResponse)
async def get_app_system_memory():
    """
        Route: `/app/system/memory`

        Return memory system page.
    """

    async with AsyncClient() as client:
        response = await client.get("http://jarjarbin.local/api/system/memory")

    return template_memory.render(title = title, version = version, memory = response.json()["data"])


@app.get("/system/battery", response_class=HTMLResponse)
async def get_app_system_battery():
    """
        Route: `/app/system/battery`

        Return battery system page.
    """

    async with AsyncClient() as client:
        response = await client.get("http://jarjarbin.local/api/system/sensors?category=battery")

    return template_battery.render(title = title, version = version, battery = response.json()["data"])


@app.get("/system/disk", response_class=HTMLResponse)
async def get_app_system_disk():
    """
        Route: `/app/system/disk`

        Return disk system page.
    """

    async with AsyncClient() as client:
        response = await client.get("http://jarjarbin.local/api/system/disk")

    return template_disk.render(title = title, version = version, disk = response.json()["data"])


@app.get("/system/network", response_class=HTMLResponse)
async def get_app_system_network():
    """
        Route: `/app/system/network`

        Return network system page.
    """

    async with AsyncClient() as client:
        response = await client.get("http://jarjarbin.local/api/system/network")

    return template_network.render(title = title, version = version, network = response.json()["data"])


@app.get("/system/processes", response_class=HTMLResponse)
async def get_app_system_processes():
    """
        Route: `/app/system/processes`

        Return processes system page.
    """

    async with AsyncClient() as client:
        response = await client.get("http://jarjarbin.local/api/system/processes")

    return template_processes.render(title = title, version = version, processes = response.json()["data"])


@app.get("/system/system", response_class=HTMLResponse)
async def get_app_system_system():
    """
        Route: `/app/system/system`

        Return system system page.
    """

    async with AsyncClient() as client:
        response = await client.get("http://jarjarbin.local/api/system/system")

    return template_system.render(title = title, version = version, system = response.json()["data"])


@app.get("/system/temperatures", response_class=HTMLResponse)
async def get_app_system_temperatures():
    """
        Route: `/app/system/temperatures`

        Return temperatures system page.
    """

    async with AsyncClient() as client:
        response = await client.get("http://jarjarbin.local/api/system/sensors?category=temperatures")

    return template_temperatures.render(title = title, version = version, temperatures = response.json()["data"])


@app.get("/system/top_processes", response_class=HTMLResponse)
async def get_app_system_top_processes():
    """
        Route: `/app/system/top_processes`

        Return top_processes system page.
    """

    async with AsyncClient() as client:
        response = await client.get("http://jarjarbin.local/api/system/processes")

    return template_top_processes.render(title = title, version = version, top_processes = response.json()["data"])
