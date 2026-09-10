import psutil


def get_processes(
    ) -> list[psutil.Process]:
    return list(psutil.process_iter())


def get_process(
        pid: int
    ) -> psutil.Process:
    return psutil.Process(pid)


def get_process_count(
    ) -> int:
    return len(psutil.pids())


def get_process_pids(
    ) -> list[int]:
    return psutil.pids()


def get_process_name(
        pid: int
    ) -> str:
    return psutil.Process(pid).name()


def get_process_status(
        pid: int
    ) -> str:
    return psutil.Process(pid).status()


def get_process_cpu_percent(
        pid: int
    ) -> float:
    return psutil.Process(pid).cpu_percent()


def get_process_memory_info(
        pid: int
    ):
    return psutil.Process(pid).memory_info()


def get_process_memory_percent(
        pid: int
    ) -> float:
    return psutil.Process(pid).memory_percent()
