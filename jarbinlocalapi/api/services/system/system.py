from typing import Any
import psutil


def get_boot_time(
    ) -> float:
    return psutil.boot_time()


def get_users(
    ) -> list[dict[str, Any]]:
    return [
        user._asdict()
        for user in psutil.users()
    ]
