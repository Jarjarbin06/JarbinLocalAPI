from typing import Any
import psutil


def get_network_interfaces(
    ) -> dict:
    interfaces = psutil.net_if_addrs()

    return {
        name: [
            address._asdict()
            for address in addresses
        ]
        for name, addresses in interfaces.items()
    }


def get_network_interface_status(
    ) -> dict:
    stats = psutil.net_if_stats()

    return {
        name: status._asdict()
        for name, status in stats.items()
    }


def get_network_io_counters(
        pernic: bool = True,
        nowrap: bool = True,
    ) -> dict[str, dict[str, Any]]:
    count = psutil.net_io_counters(pernic = pernic, nowrap = nowrap)

    return {
        name: counter._asdict()
        for name, counter in count.items()
    }


def get_network_connections(
        kind: str = "inet",
    ) -> list[Any]:
    conn = psutil.net_connections(kind = kind)

    return [
        connection._asdict()
        for connection in conn
    ]