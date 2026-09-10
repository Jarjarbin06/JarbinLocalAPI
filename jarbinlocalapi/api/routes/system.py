from typing import Literal
from fastapi import Query

from jarbinlocalapi.api import api
from jarbinlocalapi.api.services.system.overview import (
    get_overview,
    get_cpu_overview,
    get_memory_overview,
    get_disk_overview,
    get_network_overview,
    get_processes_overview,
    get_sensors_overview,
    get_system_overview,
)


#-------------------- ROOT --------------------#

@api.get("/system")
async def get_system(type: Literal[
            "cpu",
            "memory",
            "disk",
            "network",
            "processes",
            "sensors",
            "system",
        ] | None = Query(default=None)
    ):
    """
        Route: `/api/system`
               `/api/system?type=<type>`

        Return complete system information.
    """

    response = get_overview()

    if type is not None:
        return {type: response.get(type, None)} or {"message": "invalid type"}

    return response


#-------------------- SYSTEMS --------------------#

@api.get("/system/cpu")
async def get_system_cpu(category: Literal[
            "percent",
            "times",
            "times_percent",
            "count",
            "stats",
            "frequency",
            "load",
        ] | None = Query(default=None)
    ):
    """
        Route: `/api/system/cpu`
               `/api/system/cpu?type=<type>`

        Return cpu system information.
    """

    response = get_cpu_overview()

    if category is not None:
        return {category: response.get(category, None)} or {"message": "invalid type"}

    return response


@api.get("/system/memory")
async def get_system_memory(category: Literal[
            "virtual",
            "swap",
        ] | None = Query(default=None)
    ):
    """
        Route: `/api/system/memory`
               `/api/system/memory?type=<type>`

        Return memory system information.
    """

    response = get_memory_overview()

    if category is not None:
        return {category: response.get(category, None)} or {"message": "invalid type"}

    return response


@api.get("/system/disk")
async def get_system_disk(category: Literal[
            "usage",
            "partitions",
            "io",
        ] | None = Query(default=None)
    ):
    """
        Route: `/api/system/disk`
               `/api/system/disk?type=<type>`

        Return disk system information.
    """

    response = get_disk_overview()

    if category is not None:
        return {category: response.get(category, None)} or {"message": "invalid type"}

    return response


@api.get("/system/network")
async def get_system_network(category: Literal[
            "interfaces",
            "interface_status",
            "io",
            "connections",
        ] | None = Query(default=None)
    ):
    """
        Route: `/api/system/network`
               `/api/system/network?type=<type>`

        Return network system information.
    """

    response = get_network_overview()

    if category is not None:
        return {category: response.get(category, None)} or {"message": "invalid type"}

    return response


@api.get("/system/processes")
async def get_system_processes(category: Literal[
            "count",
            "pids",
            "processes",
        ] | None = Query(default=None)
    ):
    """
        Route: `/api/system/processes`
               `/api/system/processes?type=<type>`

        Return processes system information.
    """

    response = get_processes_overview()

    if category is not None:
        return {category: response.get(category, None)} or {"message": "invalid type"}

    return response


@api.get("/system/sensors")
async def get_system_sensors(category: Literal[
            "temperatures",
            "fans",
            "battery",
        ] | None = Query(default=None)
    ):
    """
        Route: `/api/system/sensors`
               `/api/system/sensors?type=<type>`

        Return sensors system information.
    """

    response = get_sensors_overview()

    if category is not None:
        return {category: response.get(category, None)} or {"message": "invalid type"}

    return response


@api.get("/system/system")
async def get_system_system(category: Literal[
            "boot_time",
            "users",
        ] | None = Query(default=None)
    ):
    """
        Route: `/api/system/system`
               `/api/system/system?type=<type>`

        Return system system information.
    """

    response = get_system_overview()

    if category is not None:
        return {category: response.get(category, None)} or {"message": "invalid type"}

    return response
