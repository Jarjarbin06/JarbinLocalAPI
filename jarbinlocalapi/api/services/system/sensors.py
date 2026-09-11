from typing import Any

import psutil


def get_temperatures(
    ) -> dict[str, list[dict[str, Any]]]:
    return {
        name: [
            temperature._asdict()
            for temperature in entries
        ]
        for name, entries in psutil.sensors_temperatures().items()
    }


def get_fans(
    ) -> dict[str, list[dict[str, Any]]]:
    return {
        name: [
            fan._asdict()
            for fan in entries
        ]
        for name, entries in psutil.sensors_fans().items()
    }


def get_battery(
    ) -> dict[str, Any] | None:
    bat = psutil.sensors_battery()

    return (
        bat._asdict()
        if bat is not None
        else None
    )
