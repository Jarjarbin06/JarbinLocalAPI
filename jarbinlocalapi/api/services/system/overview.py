from .cpu import (
    get_cpu_percent,
    get_cpu_times,
    get_cpu_times_percent,
    get_cpu_count,
    get_cpu_stats,
    get_cpu_freq,
    get_cpu_load,
)
from .disk import (
    get_disk_usage,
    get_disk_partitions,
    get_disk_io_counters,
)
from .memory import (
    get_virtual_memory,
    get_swap_memory,
)
from .network import (
    get_network_interfaces,
    get_network_interface_status,
    get_network_io_counters,
    get_network_connections,
)
from .process import (
    get_processes,
    get_process_count,
    get_process_pids,
)
from .sensors import (
    get_temperatures,
    get_fans,
    get_battery,
)
from .system import (
    get_boot_time
)
from .users import get_users


def get_cpu_overview(
    ) -> dict:
    return {
        "percent": get_cpu_percent(),
        "times": get_cpu_times(),
        "times_percent": get_cpu_times_percent(),
        "count": get_cpu_count(),
        "stats": get_cpu_stats(),
        "frequency": get_cpu_freq(),
        "load": get_cpu_load(),
    }


def get_memory_overview(
    ) -> dict:
    return {
        "virtual": get_virtual_memory(),
        "swap": get_swap_memory(),
    }


def get_disk_overview(
    ) -> dict:
    return {
        "usage": get_disk_usage(),
        "partitions": get_disk_partitions(),
        "io": get_disk_io_counters(perdisk=True),
    }


def get_network_overview(
    ) -> dict:
    return {
        "interfaces": get_network_interfaces(),
        "interface_status": get_network_interface_status(),
        "io": get_network_io_counters(pernic=True),
        "connections": get_network_connections(),
    }


def get_processes_overview(
    ) -> dict:
    return {
        "count": get_process_count(),
        "pids": get_process_pids(),
        "processes": [
            {
                "pid": process.pid,
                "name": process.name(),
                "status": process.status(),
                "cpu_percent": process.cpu_percent(),
                "memory_info": process.memory_info()._asdict(),
                "memory_percent": process.memory_percent(),
            }
            for process in get_processes()
        ],
    }


def get_sensors_overview(
    ) -> dict:
    return {
        "temperatures": {
            name: [
                temperature._asdict()
                for temperature in entries
            ]
            for name, entries in get_temperatures().items()
        },
        "fans": {
            name: [
                fan._asdict()
                for fan in entries
            ]
            for name, entries in get_fans().items()
        },
        "battery": (
            get_battery()._asdict()
            if get_battery() is not None
            else None
        ),
    }


def get_system_overview(
    ) -> dict:
    return {
        "boot_time": get_boot_time(),
        "users": [
            user._asdict()
            for user in get_users()
        ],
    }


def get_overview(
    ) -> dict:
    return {
        "cpu": get_cpu_overview(),
        "memory": get_memory_overview(),
        "disk": get_disk_overview(),
        "network": get_network_overview(),
        "processes": get_processes_overview(),
        "sensors": get_sensors_overview(),
        "system": get_system_overview(),
    }