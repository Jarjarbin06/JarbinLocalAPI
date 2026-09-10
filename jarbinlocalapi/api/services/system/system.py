import psutil


def get_boot_time(
    ) -> float:
    return psutil.boot_time()


def get_users(
    ) -> list[psutil._ntuples.suser]:
    return psutil.users()
