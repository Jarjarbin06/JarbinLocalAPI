from typing import Any
import psutil


def get_disk_usage(
        path: str = "/"
    ) -> dict:
    return psutil.disk_usage(path)._asdict()


def get_disk_partitions(
        all: bool = False,
    ) -> list[Any]:
    return [
        partition._asdict()
        for partition in psutil.disk_partitions(all = all)
    ]


def get_disk_io_counters(
        perdisk: bool = False,
        nowrap: bool = True,
    ) -> dict[str, dict[str, Any]] | None :
    disk = psutil.disk_io_counters(perdisk = perdisk, nowrap = nowrap)

    return (
        {
            name: counter._asdict()
            for name, counter in disk.items()
        }
        if disk is not None
        else None
    )
