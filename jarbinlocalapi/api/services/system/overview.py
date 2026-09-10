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
from jarbinlocalapi.api.utils.retry import retry


def get_cpu_overview(
    ) -> dict:
    return {
        "percent": retry(get_cpu_percent),
        "times": retry(get_cpu_times),
        "times_percent": retry(get_cpu_times_percent),
        "count": retry(get_cpu_count),
        "stats": retry(get_cpu_stats),
        "frequency": retry(get_cpu_freq),
        "load": retry(get_cpu_load),
    }


def get_memory_overview(
    ) -> dict:
    return {
        "virtual": retry(get_virtual_memory),
        "swap": retry(get_swap_memory),
    }


def get_disk_overview(
    ) -> dict:
    return {
        "usage": retry(get_disk_usage),
        "partitions": retry(get_disk_partitions),
        "io": retry(get_disk_io_counters),
    }


def get_network_overview(
    ) -> dict:
    return {
        "interfaces": retry(get_network_interfaces),
        "interface_status": retry(get_network_interface_status),
        "io": retry(get_network_io_counters),
        "connections": retry(get_network_connections),
    }


def get_processes_overview(
    ) -> dict:
    return {
        "count": retry(get_process_count),
        "pids": retry(get_process_pids),
        "processes": [
            {
                "pid": process.pid,
                "name": process.name(),
                "status": process.status(),
                "cpu_percent": process.cpu_percent(),
                "memory_info": process.memory_info()._asdict(),
                "memory_percent": process.memory_percent(),
            }
            for process in retry(get_processes)
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
            for name, entries in retry(get_temperatures).items()
        },
        "fans": {
            name: [
                fan._asdict()
                for fan in entries
            ]
            for name, entries in retry(get_fans).items()
        },
        "battery": (
            retry(get_battery)._asdict()
            if retry(get_battery) is not None
            else None
        ),
    }


def get_system_overview(
    ) -> dict:
    return {
        "boot_time": retry(get_boot_time),
        "users": [
            user._asdict()
            for user in retry(get_users)
        ],
    }


def get_overview(
    ) -> dict:
    return {
        "cpu": retry(get_cpu_overview),
        "memory": retry(get_memory_overview),
        "disk": retry(get_disk_overview),
        "network": retry(get_network_overview),
        "processes": retry(get_processes_overview),
        "sensors": retry(get_sensors_overview),
        "system": retry(get_system_overview),
    }