from typing import Any
import psutil


def get_cpu_percent(
        interval: float | None = None
    ) -> float:
    return psutil.cpu_percent(interval=interval)


def get_cpu_times(
    ) -> dict:
    return psutil.cpu_times()._asdict()


def get_cpu_times_percent(
    ) -> dict:
    return psutil.cpu_times_percent()._asdict()


def get_cpu_count(
        logical: bool = True
    ) -> int | None:
    return psutil.cpu_count(logical=logical)


def get_cpu_stats(
    ) -> dict:
    return psutil.cpu_stats()._asdict()


def get_cpu_freq(
        per_cpu: bool = False
    ) -> list[Any] | dict[str, Any] | None:
    freq = psutil.cpu_freq(percpu = per_cpu)

    return (
        [frequency._asdict() for frequency in freq]
        if isinstance(freq, list)
        else (
            freq._asdict()
            if freq is not None
            else None
        )
    )


def get_cpu_load(
    ) -> tuple[float, float, float]:
    return psutil.getloadavg()
